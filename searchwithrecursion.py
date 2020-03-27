Daftar = [5, 4, 3, 40, 14, 99, 75]

def carirekursi(myList, number):
    if myList[0] == number:
        return 0
    return 1 + search(myList[1:], number)

carirekursi(Daftar,14)





