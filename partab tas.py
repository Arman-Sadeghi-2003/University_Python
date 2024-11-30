import random

l = []

for i in range(30):
    l.append(random.randint(1, 6))

print(l)

l.sort()

D = {}

for x in l:
    if x not in D:
        D[x] = 1
    else:
        D[x] += 1
        
print(D)

for k,v in D.items():
    print(f"{k}:{v}",end="-->")
    for i in range(v):
        print('*',end=(''))
    print()