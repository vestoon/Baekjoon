import sys
import math
input = sys.stdin.readline

n, b = map(int, input().split())
sumX = 0
sumY = 0
for _ in range(n):
    x, y =  map(int, input().split())
    sumX += x
    sumY += y



"""
axn + bn -yn

-a -6 +5 = 0
sumX*a + b*n -sumY = 0
a = (sumY - b*n)/sumX
"""
if not sumX:
    print("EZPZ")
    exit()

p = sumY-b*n
q = sumX
g = math.gcd(p, q)
p //= g
q //= g
minus = (p<0 and q>0) or (p>0 and q<0)
p = abs(p)
q = abs(q)

if minus:
        print('-',end='')
if q == 1:
    print(p)
else:
    print(p,'/',q, sep='')
