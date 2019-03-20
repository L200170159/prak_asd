def katakan(a):
    x={"0":"","1":"Se","2":"Dua ","3":"Tiga ","4":"Empat ","5":"Lima ","6":"Enam ","7":"Tujuh ","8":"Delapan ","9":"Sembilan "}
    y={-1:"",-2:"puluh ",-3:"ratus ",-4:"ribu ",-5:"puluh ",-6:"ratus ",-7:"juta ",-8:"puluhjuta "}
    m = {-1: "", -2: "puluh ", -3: "ratus ", -4: "ribu ", -5: "puluh ", -6: "ratus ", -7: "juta ", -8: "puluh "}
    b=str(a)
    c=""
    if len(str(a))==8 and str(a)[1]>0:
        i = -1
        while i>= -len(b):
            c=x[b[i]]+m[i]+c
            i-=1
        return c
    else:
        i = -1
        while i >= -len(b):
            c = x[b[i]] + y[i] + c
            i -= 1
        return c