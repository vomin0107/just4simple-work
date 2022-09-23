import cv2
import matplotlib.image as img
import matplotlib.pyplot as plt


dir = 'C:/Users/minuk/Downloads/sample_output/image/'
file = '0331_02_00060.jpg'


image = cv2.imread(dir+file, cv2.IMREAD_COLOR)
image = cv2.resize(image, (640, 480))
plt.imshow(image)
plt.show()
cv2.imshow('sample', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = img.imread(dir+file)