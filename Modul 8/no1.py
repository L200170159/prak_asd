from Stack import Stack
def cetakHexa(d):
    f=Stack()
    listHex="0123456789ABCDEF"
    if d==0:
        f.push(0);
    while d!=0:
        sisa=d%16
        d=d//16
        f.push(listHex[sisa])
    st=''
    for i in range(len(f)):
        st=st+str(f.pop())
    return st
