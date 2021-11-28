def asalMi(i):
    if i<2:
        return False
    
    n=2
    
    while i % (n) != 0:
        n+= 1
        if n == i:
            return True

   



def superAsalMi(x):

    while asalMi(x):
        if len(str(x)) == 1:
            return True 

        else:
            x = int(str(x)[0:-1])
            superAsalMi(x)
    




















    
    
