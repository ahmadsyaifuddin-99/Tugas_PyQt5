from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QDesktopWidget
from PyQt5 import QtCore

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)
        self.button = QPushButton(self)
        self.button.setText("Button1")
        self.setGeometry(0,0,500,500)
        self.setWindowTitle("Belajar PyQt5")
        cwg = self.frameGeometry() # cek ukuran main window app kita
        cwc = QDesktopWidget().availableGeometry().center() # pada screen saya: (682,383)
        #print(cwc)
        cwg.moveCenter(cwc)
        self.move(cwg.topLeft())
        self.setFixedSize(300,300) # agar tidak bisa di-resize! icon maximize juga akan otomatis hilang
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint,False)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()