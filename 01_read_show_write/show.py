import cv2
from read import *

#Displays image inside a window
cv2.imshow('color image',img_color) 
cv2.imshow('grayscale image',img_grayscale)
cv2.imshow('unchanged image',img_unchanged)
 
# Waits for a keystroke
cv2.waitKey(0) 
 
# Destroys all the windows created
cv2.destroyAllwindows()