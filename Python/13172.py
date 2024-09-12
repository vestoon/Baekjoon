import sys
import math
input = sys.stdin.readline

mod = 1000000007


def power(n, m): # n**m
    if m == 1:
        return n

    mid = power(n, m//2)
    if m % 2:
        return (mid*mid*n) % mod
    return (mid*mid) % mod


M = int(input())
ans = 0
for _ in range(M):
    a, b = map(int, input().split())
    ans += (b*power(a, mod-2))
    ans %= mod

print(ans)


