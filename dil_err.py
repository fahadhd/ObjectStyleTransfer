import cv2
import numpy as np
img = cv2.imread('Masks/480p/bvs/bear/00000.png', 0)
kernel = np.ones((5,5), np.uint8)

dilute = cv2.dilate(img, kernel, iterations =10)
erode = cv2.erode(img,kernel, iterations =10)

dif = dilute - erode


for a in range(dif.shape[0]):
    for b in range(dif.shape[1]):
        if dif[a][b] > 0 and img[a][b] == 0:
            img[a][b] = 128

cv2.imshow("trimap",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
