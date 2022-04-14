import cv2 as cv
import numpy as np

# Read and display image
input_image = cv.imread('images/input.jpg')
cv.imshow('Hello World!',input_image)
cv.waitKey()

# Save output
cv.imwrite('output.jpg',input_image)

# Get image shape
print(input_image.shape)

cv.destroyAllWindows()