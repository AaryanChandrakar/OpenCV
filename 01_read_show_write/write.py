import cv2
from read import *

cv2.imwrite('grayscale1.jpg',img_grayscale)
cv2.imwrite('color.jpg', img_color)
cv2.imwrite('unchanged.jpg',img_unchanged)