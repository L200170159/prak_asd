class Manusia(object):
    """ class ' manusia' dengan inisiasi 'nama' """

    keadaan="lapar"
    def __init__(self,nama):
        self.nama=nama
    def ucapkanSalam(self):
        print "salaam, namaku",self.nama
    def makan(self,s):
        print "saya baru makan",s
        self.keadaan="kenyang"
    def olahraga(self,k):
        print "saya baru saja makan",k
        self.keadaan="lapar"
    def mengalikanDenganDua(self,a):
        return n*2

