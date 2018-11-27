import pyautogui
import pyperclip
import glob
import time

#Menu position: 10, 10
#Convert position: 30, 125
#STD file position: 300, 125
#FIFO file position: 300, 150
#setup filename position: 530, 160
#source filename position: 530, 415
#convertbutton position: 300, 760

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

# starting position of the working window. other positions are relative, so handled automatically!
    x = 50
    y = 50

    MoveWin(x, y)   # moves the "DPC-230 Emulation - FIFO data files conversion" window
                        # at 100, 100 position (top left corner).

    MouseMoveClick(x+50, x)

    for (file_set, file_spc) in zip(files_set, files_spc):

            dir_set = file_set
            MouseMove(x+300, y+65) #setup filename position
            Mouse3click('left', 0.1)
            # type_(dir_set)
            pyperclip.copy(dir_set)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.2)

            dir_spc = file_spc
            MouseMove(x+300, y+315) #source filename position
            Mouse3click('left', 0.1)
            # type_(dir_spc)                    
            pyperclip.copy(dir_spc)
            pyautogui.hotkey("ctrl", "v")

            time.sleep(0.2)

            MouseMoveClick(x+130, y+660)
            print("Converting file...")
            # print(dir_set)
            # print(dir_spc)

            time.sleep(2)
            
    print("Done!")


