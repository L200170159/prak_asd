def faktorPrima(x):
    prima=list()
    for i in range(2,x):
        a = True
        for j in prima:
            if(i%j==0):
                a=False
                break
        if a and x%i==0:
            prima.append(i)

    return prima