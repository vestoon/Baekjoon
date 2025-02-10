import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for x in range(2)]
"""
어차피 j 번째 열을 지나가려면 j-1번재 열을 통과해야 한다. 이를 이용해 dp를 만들어 보자 

"""

dp = [[0 for x in range(N)] for y in range(2)] # 왼쪽 위에서 시작해서 (i, j)까지의 경로의 최대값
dp[0][0] = grid[0][0] + max(0, grid[1][0])
dp[1][0] = grid[0][0] + grid[1][0]

for j in range(1, N):
    dp[0][j] = grid[0][j] + max(dp[0][j-1], dp[1][j-1] + grid[1][j], dp[0][j-1]+grid[1][j])
    dp[1][j] = grid[1][j] + max(dp[1][j-1], dp[0][j-1] + grid[0][j], dp[1][j-1]+grid[0][j])

print(dp[1][N-1])