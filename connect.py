import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QDateEdit

class DataDiriForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data_diri.ui', self)  # Memuat file .ui yang sudah didesain
        
        # Akses widget berdasarkan objectName dari Qt Designer
        self.npm_input = self.findChild(QLineEdit, 'npm_input')
        self.nama_input = self.findChild(QLineEdit, 'nama_input')
        self.kelas_input = self.findChild(QLineEdit, 'kelas_input')
        self.tempat_lahir_input = self.findChild(QLineEdit, 'tempat_lahir_input')
        self.tanggal_lahir_input = self.findChild(QDateEdit, 'tanggal_lahir_input')
        self.telepon_input = self.findChild(QLineEdit, 'telepon_input')
        self.alamat_input = self.findChild(QLineEdit, 'alamat_input')
        
        # Tombol
        self.simpan_button = self.findChild(QPushButton, 'simpan_button')
        self.edit_button = self.findChild(QPushButton, 'edit_button')
        self.hapus_button = self.findChild(QPushButton, 'hapus_button')
        self.batal_button = self.findChild(QPushButton, 'batal_button')
        
        # Hubungkan tombol dengan fungsi
        self.simpan_button.clicked.connect(self.simpan_data)
        self.edit_button.clicked.connect(self.edit_data)
        self.hapus_button.clicked.connect(self.hapus_data)
        self.batal_button.clicked.connect(self.batal)

    def simpan_data(self):
        # Ambil data dari input
        npm = self.npm_input.text()
        nama = self.nama_input.text()
        kelas = self.kelas_input.text()
        tempat_lahir = self.tempat_lahir_input.text()
        tanggal_lahir = self.tanggal_lahir_input.date().toString('dd-MM-yyyy')
        telepon = self.telepon_input.text()
        alamat = self.alamat_input.text()

        # Cetak data
        print(f"NPM: {npm}, Nama: {nama}, Kelas: {kelas}, Tempat Lahir: {tempat_lahir}, "
              f"Tanggal Lahir: {tanggal_lahir}, Telepon: {telepon}, Alamat: {alamat}")

    def edit_data(self):
        # Logic untuk mengedit data yang sudah ada
        print("Edit data")  # Ganti dengan logika edit yang diinginkan

    def hapus_data(self):
        # Logic untuk menghapus data
        print("Data telah dihapus")  # Ganti dengan logika hapus yang diinginkan
        self.clear_inputs()  # Menghapus semua input setelah menghapus

    def batal(self):
        # Logic untuk membatalkan input atau kembali ke keadaan awal
        print("Batal")  # Ganti dengan logika batal yang diinginkan
        self.clear_inputs()  # Menghapus semua input

    def clear_inputs(self):
        # Menghapus semua input
        self.npm_input.clear()
        self.nama_input.clear()
        self.kelas_input.clear()
        self.tempat_lahir_input.clear()
        self.tanggal_lahir_input.clear()
        self.telepon_input.clear()
        self.alamat_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = DataDiriForm()
    form.show()
    sys.exit(app.exec_())
