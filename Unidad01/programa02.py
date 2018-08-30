def factorial(x):
    if (x==0):
        return 1
    else:
        value=1
        for i in range(1,x+1):
            value=value*i
        return value
num=3
print("el factorial de %d es %d"%(num,factorial(num)))
