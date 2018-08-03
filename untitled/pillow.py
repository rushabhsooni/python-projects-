from PIL import Image
import cv2
#import PIL as Image
import numpy as np

print cv2.__version__
img = cv2.imread('rushabh.jpg',0)

img = Image.open("rushabh.jpg")
