def carp(n):
    #1'e gelince duracağım
    if n == 1:
        return 1
    #recursive base 
    else:
        return n*carp(n-1)
    
print(carp(5))
