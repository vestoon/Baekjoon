import math

A, B = map(int, input().split())
g = math.gcd(A, B)

print(A*B//g)
