import sys

def sol(n):
    ans = 0
    if n == 1: return 1
    for d in range(9, 1, -1):
        while n%d == 0:
            ans += 1
            n //= d
    
    if n != 1: return -1
    return ans


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(sol(N))