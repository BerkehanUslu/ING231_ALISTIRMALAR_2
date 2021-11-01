def topla(n):
    #1'e gelince duracağım
    if n == 1:
        return 1
    #recursive base 
    else:
        return n+topla(n-1)
    
print(topla(9))
