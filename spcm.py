import pyautogui
import glob
import time

#Menu position: 10, 10
#Convert position: 30, 125
#STD file position: 300, 125
#FIFO file position: 300, 150
#setup filename position: 530, 160
#source filename position: 530, 415
#convertbutton position: 300, 760

def MouseMove(x, y):
    pyautogui.moveTo(x, y)   # moves mouse to X of 100, Y of 200.
    # print(f'Mouse moved to {x}, {y} position!')


def MouseClick():
    pyautogui.click()  # click the left mouse button.

def MouseMoveClick(x, y):
    pyautogui.click(x=x, y=y)  # move to x, y, then click the left mouse button.

def Mouse2click():
    pyautogui.click(clicks=2)  # double-click the left mouse button

def Mouse3click(side, interval):
    # pyautogui.click(button='right', clicks=3, interval=0.25)  ## triple-click the right mouse button with a quarter second pause in between clicks
    pyautogui.click(button=side, clicks=3, interval=interval)  ## triple-click the right mouse button with a quarter second pause in between clicks

def type_(dir_in):
    # pyautogui.typewrite('Hello world!')
    pyautogui.typewrite(dir_in)

if __name__ == "__main__":

    dir_ = input("Dir>")+'\\'

    # print(dir_)

    files_set = glob.glob(dir_+'*.set')
    files_spc = glob.glob(dir_+'*.spc')

    # print(files_set, files_spc)

    for (file_set, file_spc) in zip(files_set, files_spc):

            # for file_spc in files_spc:

            dir_set = file_set
            MouseMove(530, 160)
            Mouse3click('left', 0.25)
            type_(dir_set)
            time.sleep(1)

            # print(dir_set)

            dir_spc = file_spc
            MouseMove(530, 415)
            Mouse3click('left', 0.25)
            type_(dir_spc)
            time.sleep(1)

            MouseMoveClick(300, 760)
            print("Converting file...")

            time.sleep(5)


            # print(dir_spc)







    # MouseMoveClick(10, 10)
    # MouseMoveClick(30, 125)
    # MouseMove(300, 125)
    # MouseMoveClick(300, 150)




    # MouseMoveClick(300, 760)



