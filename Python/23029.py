import sys
input = sys.stdin.readline

"""
dp[i][j] : j번째 음식을 먹음으로서 i번 연속으로 시식을 하게 되는 상황일 때의 최대값
i가 0일 때는 음식을 먹지 않을 때다다
"""

def sol():
    N = int(input()) # 1 <= N <= 100,000
    dp = [[0 for x in range(N)] for y in range(3)]
    food = [int(input()) for x in range(N)]
    ans = 0

    # 예외 처리
    if N == 1:
        print(food[0])
        return
    if N == 2:
        print(max(food[0]+food[1]//2, food[1]))
        return 
    
    # 여기부턴 N <= 3이 보장됨
    dp[1][0] = food[0]
    dp[0][1] = food[0]
    dp[1][1] = food[1]
    dp[2][1] = dp[1][0] + food[1]//2
    ans = max(dp[1][0], dp[1][1], dp[2][1])

    # dp
    for i in range(2, N):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])
        dp[1][i] = dp[0][i-1] + food[i]
        dp[2][i] = dp[1][i-1] + food[i]//2
        ans = max(ans, dp[1][i], dp[2][i])

    print(ans)

sol()