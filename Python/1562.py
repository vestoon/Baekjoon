N = int(input())
R = 1000000000
"""
dp 에 백트레킹을 넣어야 하나? 3차원 dp? 비트마스킹을 사용하면 사용된 숫자의 종류를 알 수 있다. 2의 10승


"""


# 길이가 j+1이고 j+1번째 수가 i 인 계단 수
# dp[i][j][k] 마지막 숫자가 i이고 길이가 j 이면서 각 숫자를 k로 사용한 경우의 수, k는 bit로 표기
dp = [[[0 for x in range(1024)] for y in range(N+1)] for z in range(10)]

for i in range(1, 10):
    dp[i][1][2**i] = 1

for j in range(1, N):
    for k in range(1024):
        dp[1][j+1][k|2**1] += dp[0][j][k]

    for i in range(1, 9):
        for k in range(1024):
            dp[i-1][j+1][k|2**(i-1)] += dp[i][j][k]
            dp[i+1][j+1][k|2**(i+1)] += dp[i][j][k]
    
    for k in range(1024):
        dp[8][j+1][k|2**8] += dp[9][j][k]

acc = 0
for i in range(10):
    acc += dp[i][N][1023]

print(acc % R)
# print(bin(1023))