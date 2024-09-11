# 사실 메모이제이션이었다니;;
import sys
input = sys.stdin.readline
INF = 1000000009

dp = [[0 for x in range(1001)] for y in range(1001)]
for cnt in range(1, 1001):  # m
    dp[cnt-1][0] = 1

    for i in range(1000):
        if not dp[cnt-1][i]:
            continue
        for d in range(1, 4):
            j = i + d
            if j > 1000:
                break
            dp[cnt][j] = (dp[cnt][j] + dp[cnt-1][i]) % INF

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    ans = 0

    print(dp[m][n])


