class MhsTIF(object):
    def __init__(self, nama, umur, kota, us):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__(self):
        x = self.nama + ', umur' + str(self.umur) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku ' + str(self.uangSaku) \
            + 'tiap bulannya.'
        return x

    def ambilNama(self):
        return self.nama
    def ambilUmur(self):
        return self.umur
    def ambilKota(self):
        return self.kotaTinggal
    def ambilUangSaku(self):
        return self.uangSaku

c0 = MhsTIF('Paijo', 21, 'Salatiga', 250000)
c1 = MhsTIF('Paijem', 20, 'Solo', 260000)
c2 = MhsTIF('Painem', 19, 'Surabaya', 300000)
c3 = MhsTIF('Paimin', 23, 'Tangerang', 250000)
c4 = MhsTIF('Poniran', 22, 'Bogor', 350000)
c5 = MhsTIF('Paino', 21, 'Sidoarjo', 450000)
c6 = MhsTIF('Paimo', 19, 'Bandung', 650000)
c7 = MhsTIF('Ratmo', 23, 'Surabaya', 2750000)
c8 = MhsTIF('Ratmi', 19, 'Cilacap', 210000)
c9 = MhsTIF('Painah', 22, 'Semarang', 565000)
c10 = MhsTIF('Sumarni', 21, 'Banjarmasin', 450000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def cariKota(target):
    z = []
    for i in Daftar:
        if i.kotaTinggal == target:
            hasil = Daftar.index(i)
            z.append(hasil)
    return z

def cariTerkecil(n):
    baru = n[0].uangSaku

    for i in range(len(n)):

        if(n[i].uangSaku<baru):

            baru = n[i].uangSaku

    return baru

def cariyangTerkecil(n):
    baru = n[0].uangSaku

    list = []

    for i in range(len(n)):

        if(n[i].uangSaku==baru):

            list.append(n[i].nama)

        elif(n[i].uangSaku<baru):

            baru = n[i].uangSaku

            list = []

            list.append(n[i].nama)

    return list

def cariDaftarUangSakuKurang(n):
    batas = 250000

    list = []

    for i in range(len(n)):

        if(n[i].uangSaku < batas):

            list.append(n[i].nama)

    return list
