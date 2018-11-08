import progressbar
from time import sleep
import sys



def drawProgressBar1(percent, barLen = 20):
    sys.stdout.write("\r")
    progress = ""
    for i in range(barLen):
        if i < int(barLen * percent):
            progress += "="
        else:
            progress += " "
    sys.stdout.write("[ %s ] %.2f%%" % (progress, percent * 100))
    sys.stdout.flush()

def drawProgressBar2(percent, barLen = 50):
    # percent float from 0 to 1. 
    sys.stdout.write("\r")
    sys.stdout.write("[{:<{}}] {:.0f}%".format("=" * int(barLen * percent), barLen, percent * 100))
    sys.stdout.flush()


bar = progressbar.ProgressBar(maxval=50, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for i in range(50):
    bar.update(i+1)
    sleep(0.01)
bar.finish()
list_ = [0.1, 0.2, 0.3, 0.4, 0.5]
drawProgressBar2(list_)