import pyautogui

## Window handling features:
list_ = pyautogui.getWindows() # returns a dict of window titles mapped to window IDs
# pyautogui.getWindow(str_title_or_int_id) # returns a “Win” object
win = pyautogui.getWindow('DPC-230 Emulation - FIFO data files conversion') # returns a “Win” object
win.move(100, 100)

# win.resize(width, height)
# win.maximize()
# win.minimize()
# win.restore()
# win.close()
win.position() # returns (x, y) of top-left corner
# win.moveRel(x=0, y=0) # moves relative to the x, y of top-left corner of the window
# win.clickRel(x=0, y=0, clicks=1, interval=0.0, button=’left’) # click relative to the x, y of top-left corner of the window

pyautogui.click(150, 110)

print(list_,'\n', win)