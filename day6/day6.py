import cv2 as cv
import numpy as np

image = cv.imread('images/input.jpg')
cv.imshow('original',image)
cv.waitKey()

height, width = image.shape[:2]

# Divide by two to rototate the image around its centre
rotation_matrix = cv.getRotationMatrix2D((width/2, height/2), 90, .5)

rotated_image = cv.warpAffine(image, rotation_matrix, (width, height))

cv.imshow('Rotated Image', rotated_image)
cv.waitKey()

#Other Option to Rotate
img = cv.imread('images/input.jpg')

rotated_image = cv.transpose(img)

cv.imshow('Rotated Image - Method 2', rotated_image)
cv.waitKey()

# Let's now to a horizontal flip.
flipped = cv.flip(image, 1)
cv.imshow('Horizontal Flip', flipped)
cv.waitKey()

# Store height and width of the image
height, width = image.shape[:2]

quarter_height, quarter_width = height/4, width/4

#       | 1 0 Tx |
#  T  = | 0 1 Ty |

# T is our translation matrix
T = np.float32([[1, 0, quarter_width], [0, 1,quarter_height]])

# We use warpAffine to transform the image using the matrix, T
img_translation = cv.warpAffine(image, T, (width, height))
cv.imshow('Translation', img_translation)
cv.waitKey()

print(T)
cv.destroyAllWindows()