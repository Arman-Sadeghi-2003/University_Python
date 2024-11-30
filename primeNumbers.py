def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True

N = int(input("N="))

counter = 0

for i in range(2, N):
    if isPrime(i):
        counter += 1
        
print("Prime numbers =",counter)