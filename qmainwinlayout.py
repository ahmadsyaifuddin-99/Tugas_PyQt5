from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QVBoxLayout

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        btn1 = QPushButton("btn1")
        btn2 = QPushButton("btn2")
        btn3 = QPushButton("btn3")
        btn4 = QPushButton("btn4")
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()