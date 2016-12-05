import cv2
import numpy as np
import subprocess
import os

def create_trimap(mask,output_dir):
	img = cv2.imread(mask, 0)
	kernel = np.ones((5,5), np.uint8)

	dilute = cv2.dilate(img, kernel, iterations =7)
	erode = cv2.erode(img,kernel, iterations =7)

	#Fills dilute color with gray and fills eroded inner section with white
	for i in range(dilute.shape[0]):
		for j in range(dilute.shape[1]):
			if(dilute[i][j] > 0 ):
				dilute[i][j] = 128

			if(erode[i][j] == 255):
				dilute[i][j] = 255


	# dif = erode-dilute
	# for a in range(dif.shape[0]):
	# 	for b in range(dif.shape[1]):
	# 		if dif[a][b] > 0 and img[a][b] == 0:
	# 			img[a][b] = 128


	#Saving trimap
	cv2.imwrite(output_dir,dilute)

	# # Testing
	cv2.imshow('image',dilute)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def main():
	#For single image
	create_trimap('Masks/480p/bvs/car-turn/00048.png','trimaps/480p/car-turn/00048.png')

	#For whole directory
	# for fn in os.listdir("Masks/480p/bvs/car-turn"):
	# 	if(fn.endswith(".png")):
	# 		create_trimap("Masks/480p/bvs/car-turn/"+fn,"trimaps/480p/car-turn/"+fn)
	


main()