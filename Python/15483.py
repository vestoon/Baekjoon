import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
N, M = len(A), len(B)

dp = [[0 for j in range(M+1)] for i in range(N+1)]

for i in range(1, N+1):
    dp[i][0] = i
for j in range(1, M+1):
    dp[0][j] = j

for i in range(1, N+1):
    for j in range(1, M+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1

print(dp[N][M])
