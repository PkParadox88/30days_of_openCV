import cv2 as cv
import numpy as np

image = cv.imread('images/input.jpg')
height, width = image.shape[:2]

# Let's get the starting pixel coordiantes (top  left of cropping rectangle)
start_row, start_col = int(height * .25), int(width * .25)

# Let's get the ending pixel coordinates (bottom right)
end_row, end_col = int(height * .75), int(width * .75)

# Simply use indexing to crop out the rectangle we desire
cropped = image[start_row:end_row , start_col:end_col]

cv.imshow("Original Image", image)
cv.waitKey(0)
cv.imshow("Cropped Image", cropped)
cv.waitKey(0)

# Create a matrix of ones, then multiply it by a scaler of 100
# This gives a matrix with same dimesions of our image with all values being 100
M = np.ones(image.shape, dtype = "uint8") * 175

# We use this to add this matrix M, to our image
# Notice the increase in brightness
added = cv.add(image, M)
cv.imshow("Added", added)
cv.waitKey(0)

# Likewise we can also subtract
# Notice the decrease in brightness
subtracted = cv.subtract(image, M)
cv.imshow("Subtracted", subtracted)
cv.waitKey(0)

cv.destroyAllWindows()