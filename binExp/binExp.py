import sys
import math

if len(sys.argv) != 4:
    print("ERROR: provide a file name")
    exit()
a = int(sys.argv[1])
m = int(sys.argv[2])
n = int(sys.argv[3])

#a = 7
#m = 17
#n = 100

#str = '{0:08b}'.format(n)
#revStr = str [::-1]
#print(str)
#print(revStr)

def findBinExp(a,n,m):
    str = '{0:08b}'.format(n)
    revStr = str [::-1]
    x = len(revStr)
    term = a
    bo = int(revStr[0])
    if bo == 1:
        product = a
    else:
        product = 1
    for i in range(1, x):
        term = (term*term)%m
        bi = int(revStr[i])
        if bi == 1:
            product = (product * term)%m
    return product

result = findBinExp(a,n,m)
print(result)
