def buatNol(m, n):
    """Menggunakan dua input"""
    matrix = [[0 for x in range(m)] for i in range(n)]
    print(matrix)

def buatNol2(m):
    matrix = [[0 for x in range(m)] for i in range(m)]
    print(matrix)

def buatIdentitas(m):
    n = m
    matrix = [[1 if j == i else 0 for j in range(m)]for i in range(n)]
    print(matrix)

buatNol(4,3)
print ("\n")
buatNol2(2)
print ("\n")
buatIdentitas(5)
