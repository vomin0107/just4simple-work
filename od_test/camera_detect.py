import time
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
import numpy as np
from PIL import Image
import warnings
from ast import literal_eval
import cv2

warnings.filterwarnings('ignore')   # Suppress Matplotlib warnings

PATH_TO_SAVED_MODEL = "models" + "\\saved_model"
PATH_TO_LABELS = "models" + "\\saved_model"
IMAGE_PATHS = ["./images/test.jpg"]

cap = cv2.VideoCapture(0)

def load_image_into_numpy_array(path):
    """Load an image from file into a numpy array.

    Puts image into numpy array to feed into tensorflow graph.
    Note that by convention we put it into a numpy array with shape
    (height, width, channels), where channels=3 for RGB.

    Args:
      path: the file path to the image

    Returns:
      uint8 numpy array with shape (img_height, img_width, 3)
    """
    return np.array(Image.open(path))

print('Loading model...', end='')
start_time = time.time()

# Load saved model and build the detection function
detect_fn = tf.saved_model.load(PATH_TO_SAVED_MODEL)

end_time = time.time()
elapsed_time = end_time - start_time
print('Done! Took {} seconds'.format(elapsed_time))

# category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)
with open(r'C:\Users\hong0\PycharmProjects\od_test\models\saved_model\label_map.pbtxt', 'r') as file:
    data = file.read().replace('\n', '')
# print(type(data))
# print(data)
category_index = literal_eval(data)
# print(eval)
# print(type(eval))
cap = cv2.VideoCapture(0)

prev_time = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cur_time = time.time()
    sec = cur_time - prev_time
    prev_time = cur_time
    fps = str(round(1 / sec, 1)) + 'fps '

    # Format the image into a PIL Image so its compatable with Edge TPU
    cv2_im = frame
    cv2_im = cv2_im[0:479, 80:559]
    cv2_im = cv2.resize(cv2_im, (512, 512))
    # pil_im = Image.fromarray(cv2_im)

    # Resize and flip image so its a square and matches training
    # pil_im.resize((512, 512))
    # pil_im.transpose(Image.FLIP_LEFT_RIGHT)
    # print(type(pil_im))
    # print(pil_im)

    input_tensor = tf.convert_to_tensor(cv2_im)
    input_tensor = input_tensor[tf.newaxis, ...]

    detections = detect_fn(input_tensor)

    # All outputs are batches tensors.
    # Convert to numpy arrays, and take index [0] to remove the batch dimension.
    # We're only interested in the first num_detections.
    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy()
                  for key, value in detections.items()}
    detections['num_detections'] = num_detections

    # detection_classes should be ints.
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

    image_np_with_detections = cv2_im.copy()

    viz_utils.visualize_boxes_and_labels_on_image_array(
        image_np_with_detections,
        detections['detection_boxes'],
        detections['detection_classes'],
        detections['detection_scores'],
        category_index,
        use_normalized_coordinates=True,
        max_boxes_to_draw=50,
        min_score_thresh=.50,
        agnostic_mode=False)


    cv2.putText(image_np_with_detections, fps, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0))
    cv2.imshow('frame', image_np_with_detections)
    # print(results)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()