import sys
from PyQt5.QtWidgets import QApplication, QWidget


app = QApplication(sys.argv)
window = QWidget()
window.setGeometry(1000, 200, 300, 150)  # (top left corner x, y, width, hight)
window.setWindowTitle('TestWindow!')


window.show()
sys.exit(app.exec_())
