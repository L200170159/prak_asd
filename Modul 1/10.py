from math import sqrt as sq

def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    D=(b**2)-(4*a*c)
    if D<0:
        return 'determinan negatif'
    else:
        return  'determinan positif'