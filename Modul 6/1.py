from C_Mahasiswa import mahasiswa
from Master import urutkan

mh1 = mahasiswa("G", 14, "N", 11000)
mh2 = mahasiswa("I", 44, "Y", 15000)
mh3 = mahasiswa("O", 19, "D", 50600)
mh4 = mahasiswa("V", 99, "A", 124000)
mh5 = mahasiswa("A", 1999, "N", 29000)

nimMH = [mh1.NIM, mh2.NIM, mh3.NIM, mh4.NIM, mh5.NIM]
usMH = [mh1.us, mh2.us, mh3.us, mh4.us, mh5.us]


a = urutkan(nimMH)
b = urutkan(usMH)

a.printMerge(nimMH)
b.printMerge(usMH)

a.printQuick(nimMH)
b.printQuick(usMH)
