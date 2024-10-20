# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coba.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# from PyQt5 import QtCore, QtGui, QtWidgets


# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(485, 295)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(50, 70, 21, 16))
#         self.label.setObjectName("label")
#         self.label_2 = QtWidgets.QLabel(self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(50, 110, 31, 16))
#         self.label_2.setObjectName("label_2")
#         self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit.setGeometry(QtCore.QRect(100, 70, 131, 20))
#         self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.SizeBDiagCursor))
#         self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.lineEdit.setObjectName("lineEdit")
#         self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_2.setEnabled(True)
#         self.lineEdit_2.setGeometry(QtCore.QRect(100, 110, 131, 20))
#         self.lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.lineEdit_2.setAutoFillBackground(False)
#         self.lineEdit_2.setObjectName("lineEdit_2")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(40, 180, 81, 41))
#         font = QtGui.QFont()
#         font.setBold(True)
#         font.setWeight(75)
#         self.pushButton.setFont(font)
#         self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(160, 180, 81, 41))
#         font = QtGui.QFont()
#         font.setBold(True)
#         font.setWeight(75)
#         font.setStrikeOut(False)
#         self.pushButton_2.setFont(font)
#         self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.pushButton_2.setAutoFillBackground(False)
#         self.pushButton_2.setObjectName("pushButton_2")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 21))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label.setText(_translate("MainWindow", "NIM"))
#         self.label_2.setText(_translate("MainWindow", "NAMA"))
#         self.pushButton.setText(_translate("MainWindow", "Testing"))
#         self.pushButton_2.setText(_translate("MainWindow", "Exit"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QDateEdit)
from PyQt5.QtCore import QDate

class ProfileForm(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Membuat label dan input field
        nim_label = QLabel('NIM:')
        self.nim_input = QLineEdit()

        nama_label = QLabel('Nama:')
        self.nama_input = QLineEdit()

        kelas_label = QLabel('Kelas:')
        self.kelas_input = QLineEdit()

        tempat_lahir_label = QLabel('Tempat Lahir:')
        self.tempat_lahir_input = QLineEdit()

        tanggal_lahir_label = QLabel('Tanggal Lahir:')
        self.tanggal_lahir_input = QDateEdit()
        self.tanggal_lahir_input.setCalendarPopup(True)
        self.tanggal_lahir_input.setDate(QDate.currentDate())

        telepon_label = QLabel('Telepon:')
        self.telepon_input = QLineEdit()

        alamat_label = QLabel('Alamat:')
        self.alamat_input = QLineEdit()

        # Membuat tombol
        simpan_button = QPushButton('Simpan')
        edit_button = QPushButton('Edit')
        hapus_button = QPushButton('Hapus')
        batal_button = QPushButton('Batal')

        # Mengatur layout grid untuk form
        grid = QGridLayout()
        grid.addWidget(nim_label, 0, 0)
        grid.addWidget(self.nim_input, 0, 1)

        grid.addWidget(nama_label, 1, 0)
        grid.addWidget(self.nama_input, 1, 1)

        grid.addWidget(kelas_label, 2, 0)
        grid.addWidget(self.kelas_input, 2, 1)

        grid.addWidget(tempat_lahir_label, 3, 0)
        grid.addWidget(self.tempat_lahir_input, 3, 1)

        grid.addWidget(tanggal_lahir_label, 4, 0)
        grid.addWidget(self.tanggal_lahir_input, 4, 1)

        grid.addWidget(telepon_label, 5, 0)
        grid.addWidget(self.telepon_input, 5, 1)

        grid.addWidget(alamat_label, 6, 0)
        grid.addWidget(self.alamat_input, 6, 1)

        # Mengatur layout horizontal untuk tombol
        hbox = QHBoxLayout()
        hbox.addWidget(simpan_button)
        hbox.addWidget(edit_button)
        hbox.addWidget(hapus_button)
        hbox.addWidget(batal_button)

        # Menyusun layout secara vertikal
        vbox = QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        # Set judul dan ukuran window
        self.setWindowTitle('Form Profile')
        self.setGeometry(100, 100, 400, 300)

        # Menghubungkan tombol dengan fungsinya
        simpan_button.clicked.connect(self.simpan_data)
        edit_button.clicked.connect(self.edit_data)
        hapus_button.clicked.connect(self.hapus_data)
        batal_button.clicked.connect(self.batal_aksi)

    def simpan_data(self):
        # Implementasi logika penyimpanan data
        print(f"Data disimpan:\nNIM: {self.nim_input.text()}\nNama: {self.nama_input.text()}\nKelas: {self.kelas_input.text()}")

    def edit_data(self):
        # Implementasi logika edit data
        print("Edit data.")

    def hapus_data(self):
        # Implementasi logika hapus data
        self.nim_input.clear()
        self.nama_input.clear()
        self.kelas_input.clear()
        self.tempat_lahir_input.clear()
        self.tanggal_lahir_input.setDate(QDate.currentDate())
        self.telepon_input.clear()
        self.alamat_input.clear()
        print("Data dihapus.")

    def batal_aksi(self):
        # Implementasi logika batal
        print("Aksi dibatalkan.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ProfileForm()
    form.show()
    sys.exit(app.exec_())
