import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0

    return value

imgL = cv2.imread('./tsukuba_l.png',0)
imgR = cv2.imread('./tsukuba_r.png',0)
cv2.imshow('l', imgL)
cv2.imshow('r', imgR)
print(imgL)
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
dst = np.empty(disparity.shape, dtype='uint8')
for y in range(disparity.shape[0]):
    for x in range(disparity.shape[1]):
        dst[y, x] = saturated(disparity[y, x])
# disparity = np.uint8(disparity)
# df = pd.DataFrame(dst)
# df.to_csv('disparity2.csv')
print(dst)
cv2.imshow('disparity', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(dst, 'gray')
plt.show()