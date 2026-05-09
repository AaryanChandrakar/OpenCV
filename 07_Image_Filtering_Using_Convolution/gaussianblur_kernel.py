import cv2
image = cv2.imread('input-image-of-wood.jpg')

"""
Apply Gaussian blur
"""
# sigmaX is Gaussian Kernel standard deviation
# ksize is kernel size
gaussian_blur = cv2.GaussianBlur(src=image, ksize=(5,5), sigmaX=0, sigmaY=0)
 
cv2.imshow('Original', image)
cv2.imshow('Gaussian Blurred', gaussian_blur)
     
cv2.waitKey()
cv2.imwrite('gaussian_blur.jpg', gaussian_blur)
cv2.destroyAllWindows()