def fib(n):
    #base case
    if n == 1 or n == 2:
        return 1
    #recursive case 
    return fib(n-1) + fib(n-2)

#ilk 30 fibonacci sayısını bulup 1 karakter bosluk birakarak ekrana yazdirir. 
for  i in range(1,31):
    print(fib(i), end=" ")


    
