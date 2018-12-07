import numpy as np
import cv2

def read_write_show(image):
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



if __name__ == "__main__":

    # cap = cv2.VideoCapture(camera_index or filename)
    cap = cv2.VideoCapture('Test_stack.avi')
    # cap = cv2.VideoCapture('Test_stack.tif')

    n = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        n += 1
        print(ret, frame, n)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', frame)
        # cv2.imshow('frame', gray) # play in gray mode
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
