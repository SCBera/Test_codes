import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon


class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(1000, 200, 300, 200)
        self.setWindowTitle('Test!')
        self.setWindowIcon(QIcon('Penguins.jpg'))
        self.show()


app = QApplication(sys.argv)

GUI = window()

sys.exit(app.exec_())
