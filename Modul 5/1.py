class MhsTIF(object):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
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
    def ambilNIM(self):
        return self.NIM
    def ambilKota(self):
        return self.kotaTinggal
    def ambilUangSaku(self):
        return self.uangSaku

c0 = MhsTIF('Paijo', 14, 'Salatiga', 250000)
c1 = MhsTIF('Paijem', 13, 'Solo', 260000)
c2 = MhsTIF('Painem', 16, 'Surabaya', 300000)
c3 = MhsTIF('Paimin', 15, 'Tangerang', 250000)
c4 = MhsTIF('Poniran', 18, 'Bogor', 350000)
c5 = MhsTIF('Paino', 17, 'Sidoarjo', 450000)
c6 = MhsTIF('Paimo', 20, 'Bandung', 650000)
c7 = MhsTIF('Ratmo', 18, 'Surabaya', 2750000)
c8 = MhsTIF('Ratmi', 22, 'Cilacap', 210000)
c9 = MhsTIF('Painah', 19, 'Semarang', 565000)
c10 = MhsTIF('Sumarni', 24, 'Banjarmasin', 450000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def swap(A,p,q):
    tmp = A[p]
    a[p]=a[q]
    a[q]=tmp

def cariPosisiYangTerkecil(A,dariSini,sampaiSini):
    posisiYangTerkecil=dariSini
    for i in range(dariSini+1,sampaiSini):
        if A[i]<A[posisiYangTerkecil]:
            posisiYangTerkecil=i
    return posisiYangTerkecil

def cariTerkecil(A):
    baru = A[0].NIM

    for i in range(len(A)):

        if(A[i].NIM<baru):

            baru = A[i].NIM

    return baru

def urutkan(A):

    baru = {}

    for i in range(len(A)):

        baru[A[i].nama] = A[i].NIM

    listofTuples = sorted(baru.items(), key=lambda x: x[1])

    for elem in listofTuples :

        print(elem[0] , ":" , elem[1] )





urutkan(Daftar)
            
