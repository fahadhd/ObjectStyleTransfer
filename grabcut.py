import numpy as np
import cv2

img = cv2.imread('video_frames/480p/bear/00000.jpg')
mask = cv2.imread('Masks/480p/bvs/bear/00000.png',0)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

rect = (0,0, 854, 480)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_MASK)


