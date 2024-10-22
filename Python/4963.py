import sys
input = sys.stdin.readline
sys.setrecursionlimit(250000)

dx = (1, -1, 0, 0, 1, 1, -1, -1)
dy = (0, 0, 1, -1, 1, -1, 1, -1)

def dfs(i, j):
    visited[i][j] = True

    for d in range(8):
        ni, nj = i+dx[d], j+dy[d]
        if 0<=ni<h and 0<=nj<w and not visited[ni][nj] and grid[ni][nj]:
            dfs(ni, nj)


while True:
    w, h = map(int, input().split())
    if not w and not h:
        break

    visited = [[False for x in range(w)] for y in range(h)]
    grid = [list(map(int, input().split())) for x in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if grid[i][j] and not visited[i][j]:
                cnt += 1
                dfs(i, j)

    print(cnt)