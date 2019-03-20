def jumlahHurufVokal(a):
    vokal= 'AIUEOaiueo'
    jumlahVokal=""
    for i in a:
        if i in vokal:
            jumlahVokal+=i
    z=(len(a),len(jumlahVokal))
    print z

def jumlahHurufKonsonan(a):
    vokal = 'AIUEOaiueo'
    jumlahVokal = ""
    for i in a:
        if i not in vokal:
            jumlahVokal += i
    z = (len(a), len(jumlahVokal))
    print z