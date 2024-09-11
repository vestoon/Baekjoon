import sys
T = int(sys.stdin.readline())
for test_case in range(T):
    n = int(sys.stdin.readline())
    dp = [0 for x in range(101)]
    for i in range(1,4):
        dp[i] = 1
    for i in range(4,6):
        dp[i] = 2
    for k in range(6,n+1):
        dp[k] = dp[k-1] + dp[k-5]
    print(dp[n])
