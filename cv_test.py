import numpy as np
import cv2

# reads the image in gray mode
image1 = cv2.imread("Penguins.jpg", 0)
# reads the image in color mode
image2 = cv2.imread("Penguins.jpg")

# display the image with title "Penguins"
cv2.imshow('Penguins in gray', image1)
cv2.imshow('Penguins in color', image2)
cv2.waitKey(5000) #wait time in milisecond
cv2.destroyAllWindows()