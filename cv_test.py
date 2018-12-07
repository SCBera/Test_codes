import numpy as np
import cv2

# reads the image in gray mode
image1 = cv2.imread("Penguins.jpg", 0)
# reads the image in color mode
image2 = cv2.imread("Penguins.jpg")

# display the image with title "Penguins"
cv2.imshow('Penguins in gray', image1)
cv2.imshow('Penguins in color', image2)
cv2.waitKey(2*1000) #wait time in milisecond
cv2.destroyWindow('Penguins in gray') # destroys specific window
cv2.waitKey(5*1000) #wait time in milisecond
cv2.destroyAllWindows()

# save image with name
cv2.imwrite("Penguins_color.jpg", image2)

