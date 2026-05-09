import cv2

# Read an image
"""
img_color = cv2.imread('test.jpg',cv2.IMREAD_COLOR)
img_grayscale = cv2.imread('test.jpg',cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread('test.jpg',cv2.IMREAD_UNCHANGED)
"""

# Read an image (using 1,0,-1)
img_color = cv2.imread('input-image-for-demo-throughout-1024x682.jpg',1)
img_grayscale = cv2.imread('input-image-for-demo-throughout-1024x682.jpg',0)
img_unchanged = cv2.imread('input-image-for-demo-throughout-1024x682.jpg',-1)