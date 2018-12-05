"""
This program is for automatic conversion of FCS data file acquired in BH.

Author: Subhas Chandra Bera, last updated, 27th Novenber, 2018

"""
# from skimage import io
import matplotlib.pyplot as plt
import pyautogui
import pyperclip
import glob
import time
import sys


def MoveWin(x, y):
    win = pyautogui.getWindow('DPC-230 Emulation - FIFO data files conversion') # returns a “Win” object
    # Current_win_pos = win.position() # returns (x, y) of top-left corner
    win.move(x, y)


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
    print("This is tested while \'DPC-230 Emulation - FIFO data files conversion\'window\
     is open and top of other windows. Please test it before actual use!\n")

    dir_ = input("Directory of files>")+'\\'

    
    # # gets the file names from the directory
    files_set = glob.glob(dir_+'*.set')
    files_spc = glob.glob(dir_+'*.spc')

    if len(files_set) == 0:
        print(" No such file in the directory!")
        exit()

# starting position of the working window.
# other positions are relative, so handled automatically!
    x = 50
    y = 50

    MoveWin(x, y)   # moves the "DPC-230 Emulation - FIFO data files conversion" window
                    # at 100, 100 position (top left corner).

    MouseMoveClick(x+50, x)
    img1 = pyautogui.pixel(x+290,y+365)

    for (file_set, file_spc) in zip(files_set, files_spc):
        img2 = pyautogui.pixel(x+290,y+365)
        # print(img1==img2)
        while img1 != img2:
            time.sleep(2)
            img2 = pyautogui.pixel(x+290,y+365)           

        dir_set = file_set
        MouseMove(x+300, y+65) #setup filename position
        Mouse3click('left', 0.1)
        # type_(dir_set) #type may take long time for longer pathname
        pyperclip.copy(dir_set)
        pyautogui.hotkey("ctrl", "v") #faster
        # time.sleep(0.2) #in second

        dir_spc = file_spc
        MouseMove(x+300, y+315) #source filename position
        Mouse3click('left', 0.1)
        # type_(dir_spc) #type may take long time for longer pathname             
        pyperclip.copy(dir_spc)
        pyautogui.hotkey("ctrl", "v") #faster
        # time.sleep(0.2) #in second

        MouseMove(x+300, y+475) #source filename position
        Mouse3click('left', 0.1)
        # type_(dir_spc) #type may take long time for longer pathname             
        pyperclip.copy(dir_spc[:-4]+'_cnvrtd.sdt')
        pyautogui.hotkey("ctrl", "v") #faster
        # time.sleep(0.2) #in second

        # im = pyautogui.screenshot(region=(260,400, 90, 50))
        # img1 = im.getpixel((320,430))
        

        MouseMoveClick(x+130, y+660)
        print("Converting file...")
        # print(dir_set)
        # print(dir_spc)
        ## carefully choose this to avoid file skipping for longer conversion time
        # time.sleep(5) #in second
            
    print("Done!")


## Window handling features:
# pyautogui.getWindows() # returns a dict of window titles mapped to window IDs
# pyautogui.getWindow(str_title_or_int_id) # returns a “Win” object
# win.move(x, y)
# win.resize(width, height)
# win.maximize()
# win.minimize()
# win.restore()
# win.close()
# win.position() # returns (x, y) of top-left corner
# win.moveRel(x=0, y=0) # moves relative to the x, y of top-left corner of the window
# win.clickRel(x=0, y=0, clicks=1, interval=0.0, button=’left’) # click relative to the x, y of top-left corner of the window
