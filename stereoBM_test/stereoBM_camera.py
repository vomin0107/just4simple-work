import time
import numpy as np
from multiprocessing import Process, Queue
import cv2
from matplotlib import pyplot as plt


def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0

    return value


def cam(cid, result):
    cap = cv2.VideoCapture(cid)
    cap.set(3, 360)
    cap.set(4, 360)

    frame_name = 'frame' + str(cid)
    # prev_time = 0
    count = 0
    while True:
        ret, frame = cap.read()  # Read 결과와 frame

        # print(type(frame))

        # cur_time = time.time()
        # sec = cur_time-prev_time
        # prev_time = cur_time
        # fps = str(round(1/sec, 1))

        if ret:
            # if count % 30 == 0:
            #     result.put(frame.copy())
        #     cv2.putText(frame, fps, (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
            cv2.imshow(frame_name, frame)  # 컬러 화면 출력
        if cv2.waitKey(33) == 27:
            # result.put('STOP')
            break
        count += 1

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    result0 = Queue()
    result1 = Queue()
    th1 = Process(target=cam, args=(0, result0))
    th2 = Process(target=cam, args=(1, result1))

    th1.start()
    th2.start()

    print('processes started.')
    #
    # while True:
    #     # print(cnt)
    #     f0 = result0.get()
    #     f1 = result1.get()
    #
    #     f0_grey = cv2.cvtColor(f0, cv2.COLOR_BGR2GRAY)
    #     f1_grey = cv2.cvtColor(f1, cv2.COLOR_BGR2GRAY)
    #
    #     stereo = cv2.StereoSGBM_create(numDisparities=112, blockSize=9)
    #     disparity = stereo.compute(f0_grey, f1_grey)
    #     # disparity = np.uint8(disparity)
    #
    #     dst = np.empty(disparity.shape, dtype='uint8')
    #     for y in range(disparity.shape[0]):
    #         for x in range(disparity.shape[1]):
    #             dst[y, x] = saturated(disparity[y, x])
    #
    #     cv2.imshow('disparity', dst)
    #
    #     # cv2.imshow('frameL', f0)
    #     # cv2.imshow('frameR', f1)
    #     if cv2.waitKey(33) == 27:
    #         break
    #     # plt.imshow(disparity, 'gray')
    #     # plt.show()

    cv2.destroyAllWindows()
    th1.join()
    th2.join()