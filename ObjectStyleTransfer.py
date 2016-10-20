import numpy as np
import cv2

def maskImage():
	img = cv2.imread('test_video_frames/480p/bear/00000.jpg')
	mask = cv2.imread('Masks/480p/bvs/bear/00000.png',0)
	res = cv2.bitwise_and(img,img,mask = mask)
	cv2.imshow('image',res)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def main():
	maskImage()

main()