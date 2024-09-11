T = int(input())
dp = [0 for x in range(12)]
dp[0] = 1

for x in range(1, 11):
    dp[x] = dp[x-1]+dp[x-2]+dp[x-3]

for test in range(T):
    n = int(input())
    print(dp[n])


