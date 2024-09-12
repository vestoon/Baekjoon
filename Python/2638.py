import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for x in range(N)]  # 1 if there is cheese
air = [[False for x in range(M)] for y in range(N)]  # False if it is enclosed


# Suppose it is performed (r,c) is not enclosed, and make connected air not enclosed
def dfs(r, c):
    air[r][c] = True
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0 and not air[nr][nc]:
            dfs(nr, nc)


# Since edge must be enclosed, perform dfs
dfs(0, 0)

time = -1
clear = False  # True if there is no cheese
while not clear:
    melt = []  # Cheese will be melted after time
    clear = True
    for i in range(N):
        for j in range(M):
            if grid[i][j]:
                clear = False
                count = 0  # Number of air around the cheese
                for n in range(4):
                    ni, nj = i + dx[n], j+dy[n]
                    if 0 <= ni < N and 0 <= nj < M:
                        if air[ni][nj]:
                            count += 1

                if count >= 2:
                    melt.append((i, j))

    for cheese in melt:
        # Change cheese to air and perform dfs
        grid[cheese[0]][cheese[1]] = 0
        dfs(cheese[0], cheese[1])
    time += 1

print(time)
