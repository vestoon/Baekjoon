N = int(input())


dp = [0 for x in range(1001)]
dp[1] = 1
dp[2] = 3

for x in range(3, N+1):
    dp[x] = dp[x-1]+ 2*dp[x-2]

print(dp[N] % 10007)

# def dp2(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         print("n: ", n)
#         return dp(n-1) + dp(n-2)
#

# print(dp(N) % 10007)



