import numpy as np
import cv2
import subprocess


def object_style_transfer():
	
	#Todo: Put the following in a loop and save all the output files in object_style_transfers/480p/bear
	#Mask to be used to crop the stylized object from its image
	mask_for_stylized = cv2.imread('Masks/480p/bvs/bear/00000.png', 0)

	#Inverts the mask.
	#To be used on the original image to replace object with stylized object.
	mask_for_original = 255 - mask_for_stylized

	#Todo: Figure out how to get file names of images in the loop
	original_img = cv2.imread("video_frames/480p/bear/00000.jpg")

	#Todo:Instead of dest.img use images in stylized_video_frames/480p/bear_stylized_resized
	stylized_img = cv2.imread("dest.jpg")
	
	stylized_cropped = cv2.bitwise_and(stylized_img,stylized_img,mask = mask_for_stylized)
	original_cropped = cv2.bitwise_and(original_img,original_img,mask = mask_for_original)

	#Final image of the object style transfer
	object_stylized_img = cv2.bitwise_or(stylized_cropped,original_cropped)

	#Testing
	# cv2.imshow('image',object_stylized_img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()




def main():
	#Resizes stylized images in a directory to be the same width and height as mask
	#resize_images(854,480,"stylized_video_frames/480p/bear_stylized")

	object_style_transfer()


main()



##### Helper Functions #####

def resize_images(width,height,image_folder):
	output_folder = "bear_stylized_resized"

	subprocess.check_call(["mogrify","-path",output_folder,"-resize",
		str(width)+'x'+str(height)+'!',"-format","jpg","*.jpg"],cwd=image_folder)