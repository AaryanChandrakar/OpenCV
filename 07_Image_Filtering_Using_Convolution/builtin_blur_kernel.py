import cv2
image = cv2.imread('input-image-of-wood.jpg')

"""
Apply blur using `blur()` function
"""
img_blur = cv2.blur(src=image, ksize=(5,5)) # Using the blur function to blur an image where ksize is the kernel size
 
# Display using cv2.imshow()
cv2.imshow('Original', image)
cv2.imshow('Blurred', img_blur)
 
cv2.waitKey()
cv2.imwrite('blur.jpg', img_blur)
cv2.destroyAllWindows()