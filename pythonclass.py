from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel

class MyWindow(QMainWindow): 
    def _init__(self): 
        super()._init__()
        self.label = QLabel(self) 
        self.label.setText("Labell") 
        self.label.move(200, 0) 
        self.button = QPushButton(self) 
        self.button.setText("Button1")
    
app = QApplication([]) 
window = MyWindow() 
window.show() 
app.exec_()