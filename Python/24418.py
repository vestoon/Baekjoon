import sys

N = int(input())
matrix = [list(map(int, input().split())) for y in range(N)]

dp = [[0 for x in range(N+1)] for y in range(N+1)]
for i in range(1, N+1):
    dp[0][i] = 1
    dp[i][0] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[N][N])
print(N*N)