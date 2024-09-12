import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())
V = list(map(int, input().split()))
dp = [False for x in range(M+1)]
dp[S] = True
for v in V:
    tmp = [False for x in range(M+1)]

    for i in range(M+1):
        if not dp[i]:
            continue
        if i+v <= M:
            tmp[i+v] = True
        if i-v >= 0:
            tmp[i-v] = True

    dp = tmp

ans = -1
for i in range(M, -1, -1):
    if dp[i]:
        ans = i
        break
print(ans)
