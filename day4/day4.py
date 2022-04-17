import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

image = cv.imread('images/tobago.jpg')

# Plot Histogram
histogram = cv.calcHist([image],[0],None,[256],[0,256])
plt.hist(image.ravel(),256,[0,256])
plt.show()

# Seperate colors
color = ('b','g','r')

for i,col in enumerate(color):
    histogram2 = cv.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histogram2,color = col)
    plt.xlim([0,256])
plt.show()
