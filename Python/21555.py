import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0 for x in range(N)] for y in range(2)]
dp[0][0] = A[0]
dp[1][0] = B[0]

for i in range(1, N):
    dp[0][i] = min(dp[0][i-1]+A[i], dp[1][i-1]+A[i]+K)
    dp[1][i] = min(dp[0][i-1]+B[i]+K, dp[1][i-1]+B[i])

print(min(dp[0][-1], dp[1][-1]))

# for _ in dp:
#     print(_)