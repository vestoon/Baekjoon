"""
매개변수 탐색 원래 이렇게 하는건데 이전엔 왜 그랬는지
이게 훨씬 코드도 간단하고 빠르다
"""
import sys
input= sys.stdin.readline

N, M, K = map(int, input().split())

beers = []
maxC = 0
for _ in range(K):
    v, c = map(int, input().split())
    maxC = max(maxC, c)
    beers.append((v, c))
beers.sort(reverse=True)

lo = 0
hi = maxC


def check(x):
    cnt = 0
    acc = 0
    for v, c in beers:
        if c <= x:
            acc += v
            cnt += 1
        if cnt == N:
            break

    return acc >= M and cnt == N


if not check(hi):
    print(-1)
    exit()

while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid):
        hi = mid
    else:
        lo = mid

print(hi)


