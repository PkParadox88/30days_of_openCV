import cv2 as cv

image = cv.imread('images/input.jpg')
cv.imshow('original',image)
cv.waitKey()

# Let's make our image 3/4 of it's original size
image_scaled = cv.resize(image, None, fx=0.75, fy=0.75)
cv.imshow('Scaling - Linear Interpolation', image_scaled) 
cv.waitKey()

# Let's double the size of our image
img_scaled = cv.resize(image, None, fx=2, fy=2, interpolation = cv.INTER_CUBIC)
cv.imshow('Scaling - Cubic Interpolation', img_scaled)
cv.waitKey()

# Let's skew the re-sizing by setting exact dimensions
img_scaled = cv.resize(image, (900, 400), interpolation = cv.INTER_AREA)
cv.imshow('Scaling - Skewed Size', img_scaled) 
cv.waitKey()

# Image Pyramids
smaller = cv.pyrDown(image)
larger = cv.pyrUp(smaller)

cv.imshow('Smaller ', smaller )
cv.waitKey(0)
cv.imshow('Larger ', larger )
cv.waitKey(0)

cv.destroyAllWindows()