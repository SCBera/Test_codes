import numpy as np
import pylab
from scipy import ndimage
import cv2

def read_write_show(image):
    # reads the image in gray mode
    image1 = cv2.imread(image, 0)
    # reads the image in color mode
    image2 = cv2.imread(image)

    # display the image with title "Penguins"
    cv2.imshow('Penguins in gray', image1)
    cv2.imshow('Penguins in color', image2)
    cv2.waitKey(2*1000) #wait time in milisecond
    cv2.destroyWindow('Penguins in gray') # destroys specific window
    cv2.waitKey(5*1000) #wait time in milisecond
    cv2.destroyAllWindows()

    # save image with name
    cv2.imwrite("Penguins_color.jpg", image2)

def read_sequence(stack):
    # cap = cv2.VideoCapture(camera_index or filename)
    cap = cv2.VideoCapture('stack.avi')
    # cap = cv2.VideoCapture('Test_stack.tif')

    n = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        n += 1
        print(ret, frame, n)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        cv2.imshow('frame', frame)
        # cv2.imshow('frame', gray) # play in gray mode
        if cv2.waitKey(1000) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def count_particles(imagefile):
    im = cv2.imread(imagefile)
    pylab.figure(0)
    pylab.imshow(im)

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    maxValue = 355
    adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C#cv2.ADAPTIVE_THRESH_MEAN_C #cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    thresholdType = cv2.THRESH_BINARY#cv2.THRESH_BINARY #cv2.THRESH_BINARY_INV
    blockSize = 5 #odd number like 3,5,7,9,11
    C = -3 # constant to be subtracted
    im_thresholded = cv2.adaptiveThreshold(gray, maxValue, adaptiveMethod, thresholdType, blockSize, C) 
    labelarray, particle_count = ndimage.measurements.label(im_thresholded)
    print(particle_count)
    pylab.figure(1)
    pylab.imshow(im_thresholded)
    pylab.show()


if __name__ == "__main__":

    # im = cv2.imread('test_circles.jpg')
    count_particles('test_circles.jpg')
