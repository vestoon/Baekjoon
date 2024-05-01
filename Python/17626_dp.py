n = int(input())

dp = [0 for x in range(n+1)]
dp[1] = 1

for i in range(2, n+1):

    j = 1
    while j**2 <= i:
        dp[i] = min(dp[i-j**2] + 1, dp[i]) if dp[i] else dp[i-j**2] + 1
        j += 1

print(dp[-1])