import sys
from math import gcd
input = sys.stdin.readline

N = int(input())
radius = list(map(int, input().split()))

r = radius[0]

# def gcd(a:int, b:int) ->int:
#     if b == 0:
#         return a

#     r = a%b
#     return gcd(b, r)

for i in range(1, N):
    g = gcd(r, radius[i])
    print(r//g, '/', radius[i]//g, sep='')