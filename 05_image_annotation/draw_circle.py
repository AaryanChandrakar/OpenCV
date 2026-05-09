import cv2
# Read Images
img = cv2.imread('sample.jpg')
# Make a copy of image
imageCircle = img.copy()
# define the center of circle
circle_center = (415,190)
# define the radius of the circle
radius =100
#  Draw a circle using the circle() Function
cv2.circle(imageCircle, circle_center, radius, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)
# Display the result
cv2.imshow("Image Circle",imageCircle)
cv2.waitKey(0)
cv2.destroyAllWindows()