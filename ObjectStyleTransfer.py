import numpy as np
import cv2
import subprocess
import os


def object_style_transfer(img_name,masks_dir,original_dir,stylized_dir):
	
	#Todo: Put the following in a loop and save all the output files in object_style_transfers/480p/bear
	#Mask to be used to crop the stylized object from its image
	img_mask = img_name+'.png'
	img_file = img_name+'.jpg'
	# mask_for_stylized = cv2.imread("Masks/480p/bvs/bear/"+img_mask, 0)
	mask_for_stylized = cv2.imread(masks_dir+img_mask, 0)

	#Inverts the mask.
	#To be used on the original image to replace object with stylized object.
	mask_for_original = 255 - mask_for_stylized

	#Todo: Figure out how to get file names of images in the loop
	# original_img = cv2.imread("video_frames/480p/bear/"+img_file)
	original_img = cv2.imread(original_dir+img_file)

	#Todo:Instead of dest.img use images in stylized_video_frames/480p/bear_stylized_resized
	stylized_img = cv2.imread(stylized_dir+img_file)
	
	stylized_cropped = cv2.bitwise_and(stylized_img,stylized_img,mask = mask_for_stylized)
	original_cropped = cv2.bitwise_and(original_img,original_img,mask = mask_for_original)

	#Final image of the object style transfer
	object_stylized_img = cv2.bitwise_or(stylized_cropped,original_cropped)

	cv2.imwrite("object_style_transfers/480p/bear/"+img_file,object_stylized_img)
	#Testing
	# cv2.imshow('image',object_stylized_img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()




def main():
	#Resizes stylized images in a directory to be the same width and height as mask
	#resize_images(854,480,"stylized_video_frames/480p/bear_stylized")



	for fn in os.listdir("stylized_video_frames/480p/bear_stylized"):
		if(fn.endswith(".jpg")):
			img_name = fn.rsplit('.', 1)[0]
			object_style_transfer(img_name,"Masks/480p/bvs/bear/","video_frames/480p/bear/",
						  "stylized_video_frames/480p/bear_stylized_resized/")



main()



##### Helper Functions #####

#Resizes stylized images in a directory to be the same width and height as mask
#ex resize_images(854,480,"stylized_video_frames/480p/bear_stylized")
def resize_images(width,height,image_folder):
	output_folder = "bear_stylized_resized"

	subprocess.check_call(["mogrify","-path",output_folder,"-resize",
		str(width)+'x'+str(height)+'!',"-format","jpg","*.jpg"],cwd=image_folder)