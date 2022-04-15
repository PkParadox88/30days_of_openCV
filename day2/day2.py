import cv2 as cv

# image input
image = cv.imread('images/input.jpg')
cv.imshow('original',image)
cv.waitKey()

# convert to Grayscale
gray_image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('grayscale',gray_image)
cv.waitKey()

# Another method to convert to grayscale
image2 = cv.imread('images/input.jpg',0)
cv.imshow('easy grayscale',image2)
cv.waitKey()

cv.destroyAllWindows()