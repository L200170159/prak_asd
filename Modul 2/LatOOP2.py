class Pesan(object):
    """
        sebuah class bernama Pesan.
        untuk memahami konsep class dan object
    """

    def __init__(self,sebuahString):
        self.teks=sebuahString
    def cetakIni(self):
        print self.teks
    def cetakHurufKapital(self):
        print str.upper(self.teks)
    def cetakHurufKecil(self):
        print str.lower(self.teks)
    def jumKar(self):
        return len(self.teks)
    def cetakJumKar(self):
        print "kalimatku mempunyai ",len(self.teks),"karakter"
    def perbarui(self,baru):
        self.teks=baru
    def apakahTerkandung(self,kata):
        if kata in self.teks:
            return True
        else:
            return False
    def hitungKonsonan(self):
        vokal = 'AIUEOaiueo'
        jumlahVokal = ""
        for i in self.teks:
            if i not in vokal:
                jumlahVokal += i
        z = (len(jumlahVokal))
        print z

    def hitungVokal(self):
        vokal = 'AIUEOaiueo'
        jumlahVokal = ""
        for i in self.teks:
            if i in vokal:
                jumlahVokal += i
        z = (len(jumlahVokal))
        print z