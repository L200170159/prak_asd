from latOOP3 import Manusia
class Mahasiswa(Manusia):
    """ Class Mahasiswa yang dibangun dari Class Manusia"""
    listKuliah=[]
    def __init__(self,nama,NIM,kota,us):
        self.nama=nama
        self.NIM=NIM
        self.KotaTinggal=kota
        self.UangSaku=us
    def __str__(self):
        s=self.nama+" ,NIM"+str(self.NIM)\
        +". Tinggal di "+self.KotaTinggal\
        +". Uangsaku RP. "+str(self.UangSaku)\
        +"tiap bulannya"
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.UangSaku
    def makan(self,s):
        print "saya baru saja makan ",s," sambil belajar"
        self.keadaan="kenyang"
    def ambilKotaTinggal(self):
        return self.KotaTinggal
    def perbaharuiKotaTinggal(self,a):
        self.KotaTinggal=a
    def tambahUangSaku(self,n):
        self.UangSaku+=n

    def ambilKuliah(self,i):
        self.listKuliah.append(i)

    def HapusMakul(self,i):
        self.listKuliah.remove(i)

nama=input("Input Nama       :")
NIM=input("Input NIM        :")
KotaTinggal=input("Input Kota Asal  :")
UangSaku=input("Input Uang Saku  :")
obj=Mahasiswa(nama,NIM,KotaTinggal,UangSaku)
