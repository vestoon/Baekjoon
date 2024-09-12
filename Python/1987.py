import sys
input = sys.stdin.readline
R, C = map(int, input().split())

board = []
for row in range(R):
    board.append(input())

used = [False for x in range(26)]
visited = [[False for x in range(C)] for y in range(R)]
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)


def dfs(r, c):
    asci = ord(board[r][c])-65
    used[asci] = True
    visited[r][c] = True
    ret = 0

    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if (0 <= nr < R) and (0 <= nc < C) and (not used[ord(board[nr][nc])-65]) and (not visited[nr][nc]):
            ret = max(ret, dfs(nr, nc))

    used[asci] = False
    visited[r][c] = False
    return ret+1


print(dfs(0, 0))
