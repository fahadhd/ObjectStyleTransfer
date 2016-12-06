import numpy as np
import cv2
import subprocess
import os


def object_style_transfer(img_name,masks_dir,original_dir,stylized_dir,output_dir):
	img_mask = img_name+'.png'
	img_file = img_name+'.jpg'
	mask_for_stylized = cv2.imread(masks_dir+img_mask, 0)

	#Inverts the mask so original image has a cropped section 
	#where stylized object will be placed.
	mask_for_original = 255 - mask_for_stylized

	original_img = cv2.imread(original_dir+img_file)

	stylized_img = cv2.imread(stylized_dir+img_file)
	
	#Appliyng masks to original and stylized images

	original_cropped = cv2.bitwise_and(original_img,original_img,mask = mask_for_original)
	stylized_cropped = cv2.bitwise_and(stylized_img,stylized_img,mask = mask_for_stylized)
	

	#Final image of the object style transfer
	object_stylized_img = cv2.bitwise_or(stylized_cropped,original_cropped)

	#Saving image
	#cv2.imwrite(output_dir+img_file,object_stylized_img)

	#Testing
	cv2.imshow('image',object_stylized_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()



######################### Helper Functions ########################

#Resizes stylized images in a directory to be the same width and height as mask
#ex resize_images(854,480,"stylized_video_frames/480p/bear_stylized")
def resize_images(width,height,image_folder,output_dir):

	subprocess.check_call(["mkdir",output_dir],cwd=image_folder)

	subprocess.check_call(["mogrify","-path",output_dir,"-resize",
		str(width)+'x'+str(height)+'!',"-format","jpg","*.jpg"],cwd=image_folder)

	subprocess.check_call(["mv",output_dir,"../"],cwd=image_folder)


def main():
	original_dir = "video_frames/480p/blackswan"

	stylized_dir = "stylized_video_frames/480p/blackswan-stylized"

	output_dir = "object_style_transfers/480p/blackswan"

	#Stylized images need to be resized to mask width and height prior to object style transfer
	#Resizes stylized images in a directory to be the same width and height as mask
	#resize_images(854,480,"stylized_video_frames/480p/blackswan-stylized","blackswan-stylized-resized")

	resized_dir = "stylized_video_frames/480p/blackswan-stylized-resized"

	masks_dir = "Masks/480p/bvs/blackswan"

	object_style_transfer('00000',masks_dir,original_dir,resized_dir,output_dir)

	#Loops through a directory of images, applies object style transfer, and saves results
	# for fn in os.listdir(original_dir):
	# 	if(fn.endswith(".jpg")):
	# 		img_name = fn.rsplit('.', 1)[0]
	# 		object_style_transfer(img_name,masks_dir,original_dir,resized_dir,output_dir)



main()
