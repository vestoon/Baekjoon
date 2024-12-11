import sys
import math
input = sys.stdin.readline

def substraction(a1, b1, a2, b2): # a1/b1 - a2/b2
    x = a1*b2 - a2*b1 # return x/y
    y = b1*b2
    g = math.gcd(x, y)

    return x//g, y//g

while True:
    M, N = map(int, input().split())
    if not (M or N): break

    a, b = M, N
    n = 1 # 1/n
    while a:
        if  a*n < b: # a/b < 1/n
            n += 1
            continue
        na, nb = substraction(a, b, 1, n)
        if 1000000 < nb:
            n += 1
        else:
            a, b = na, nb
            print(n, end=' ')

    print()
    




