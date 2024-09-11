import sys
N = int(sys.stdin.readline())  # 300 이하 자연수

stairs = [0]
# visited = [0 for x in range(N+1)]
dp = [0 for x in range(N+1)]
for g in range(N):
    stairs.append(int(sys.stdin.readline()))


dp[1] = stairs[1]
if N >= 2:
    dp[2] = dp[1] + stairs[2]
if N >= 3:
    dp[3] = max(stairs[1]+stairs[3], stairs[2] + stairs[3])
    for n in range(4, N+1):
        dp[n] = max(dp[n-2]+stairs[n], dp[n-3]+stairs[n-1]+stairs[n])

print(dp[-1])
