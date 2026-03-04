# from math import gcd 있음
def gcd(n, m):
  if m == 0:
    return n
  return gcd(m, n%m)

n, m = map(int, input().split(":"))
g = gcd(n, m)
print(f"{n//g}:{m//g}")