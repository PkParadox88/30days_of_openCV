import cv2 as cv
import numpy as np

# Create a black image
image = np.zeros((512,512,3), np.uint8)

# Make B&W
image_bw = np.zeros((512,512), np.uint8)

cv.imshow("Black Rectangle (Color)", image)
# cv.imshow("Black Rectangle (B&W)", image_bw)
cv.waitKey()

# Draw a line
cv.line(image,(0,0),(511,511),(255,127,0),5)
cv.imshow('line',image)
cv.waitKey(0)

# Draw a rectangle
cv.rectangle(image, (100,100), (300,250), (127,50,127), -1)
cv.imshow("Rectangle", image)
cv.waitKey(0)

# Draw a circle
cv.circle(image, (350, 350), 100, (15,75,50), -1)
cv.imshow("Circle", image)
cv.waitKey(0)

# Draw a polygon
pts = np.array( [[10,50], [400,50], [90,200], [50,500]], np.int32)
pts = pts.reshape((-1,1,2))

cv.polylines(image, [pts], True, (0,0,255), 3)
cv.imshow("Polygon", image)
cv.imwrite('draw.jpg',image)
cv.waitKey(0)

# Write Text
cv.putText(image, 'Hello World!', (75,290), cv.FONT_HERSHEY_COMPLEX, 2, (100,170,0), 3)
cv.imshow("Hello World!", image)
cv.waitKey(0)

cv.destroyAllWindows()