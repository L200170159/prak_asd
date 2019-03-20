from latOOP3 import Manusia
class SiswaSMA(Manusia):
    def __init__(self,nama,nisn,alamat):
        self.nama=nama
        self.nisn=nisn
        self.alamat=alamat
    def ambilNama(self):
        return self.nama
    def ambilNISN(self):
        return self.nisn
    def ambilAlamat(self):
        return self.alamat
    def updateAlamat(self,a):
        self.alamat=a
