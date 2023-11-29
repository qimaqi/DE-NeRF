import cv2 
import os 
import glob
import shutil
import numpy as np 


"""
check rgba image to grayscale
"""
imgs_path = 'dynamic_lego/rgb'
imgs_files = sorted(glob.glob(os.path.join(imgs_path,'*.png')))

depth_path = 'dynamic_lego/depth'
depth_files = sorted(glob.glob(os.path.join(depth_path,'*.png')))


def read_rgba(image_path, depth_file):
    gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    depth_img = cv2.imread(depth_file, cv2.IMREAD_UNCHANGED)[...,0]
    depth_img[depth_img>0] = 1
    gray_img = gray_img*depth_img + 255 * (1-depth_img)
    return gray_img


for image_file, depth_file in zip(imgs_files, depth_files):
    image = read_rgba(image_file, depth_file)
    new_path = image_file.replace('rgb','grayscale')
    cv2.imwrite(new_path, image)