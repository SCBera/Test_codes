# import pywinauto
# from pywinauto import application
from pywinauto.application import application

app = application(backend="uia").Start(cmd_line=u'"C:\\Windows\\system32\\calc.exe" ')
calcframe = app.CalcFrame
calcframe.Wait('ready')
button = calcframe.Button13
button.Click()
button2 = calcframe.Button23
button2.Click()
button3 = calcframe.Button17
button3.Click()
button4 = calcframe.Button30
button4.Click()

app.Kill_()

input('Done!')