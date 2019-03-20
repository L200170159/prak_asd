def HitungPrima(x):
    prima=list()
    for i in range(2,x):
           a = True
           for j in prima:
               if(i%j==0):
                a=False
                break
           if(a):
               print(i)
               prima.append(i)