# Second version
# Get better time complexity with same memory
# Improvement: Since save visit count in dfs, we don't need to check the cheese will melt next time!
import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for x in range(N)]  # 1 if there is cheese
air = [[0 for x in range(M)] for y in range(N)]  # 0: enclosed air, else: visited count of cheese(1 can be air not cheese)


# Suppose it is performed (r,c) is not enclosed, and make connected air not enclosed
def dfs(r, c):
    air[r][c] = True
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if 0 <= nr < N and 0 <= nc < M:
            if grid[nr][nc]:
                air[nr][nc] += 1
            elif air[nr][nc] == 0:
                air[nr][nc] = 1
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
                if air[i][j] >= 2:
                    melt.append((i, j))

    for cheese in melt:
        # Change cheese to air and perform dfs
        grid[cheese[0]][cheese[1]] = 0
        dfs(cheese[0], cheese[1])
    time += 1

print(time)
