import sys
input = sys.stdin.readline

dx = (0, -1, -1, 0, 1, 1)
dy = (-1, -1, 0, 1, 1, 0)

# dp[x][y][t] : t번 움직였을 때 (x, y)에 도달하는 경우의 수
dp = [[[0 for x in range(30)] for y in range(30)] for t in range(15)]
dp[0][0][0] = 1

# t 에서 t+1로 넘어갈 때
for t in range(14):
    # print('t', t)
    for i in range(30):
        for j in range(30):
            if not dp[t][i][j]: continue
            # print('i j', i, j)
            for d in range(6):
                ni, nj = (i+dx[d])%30, (j+dy[d])%30
                # print('ni nj', ni, nj)
                dp[t+1][ni][nj] += dp[t][i][j]



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    print(dp[n][0][0])