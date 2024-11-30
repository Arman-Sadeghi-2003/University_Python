def power(a,b):
    if a <= 0 and b < 0:
        return 0
    elif b == 0:
        return 1
    
    else:
        return a * power(a, b-1)
    

print(power(2,10))