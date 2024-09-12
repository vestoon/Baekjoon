import collections
import sys
N = int(sys.stdin.readline())
grid = []
visited = [[False for x in range(N)] for y in range(N)]
for x in range(N):
    line = sys.stdin.readline().rstrip()
    grid.append(line)

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)


def BFS(cor, color):
    q = collections.deque()
    q.append(cor)
    visited[cor[0]][cor[1]] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < N and 0 <= ny < N) and (not visited[nx][ny]) and (grid[nx][ny] == color):
                q.append((nx, ny))
                visited[nx][ny] = True


def BFS_RG(cor, color):
    if color != 'B':
        color = "RG"
    q = collections.deque()
    q.append(cor)
    visited[cor[0]][cor[1]] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < N and 0 <= ny < N) and (not visited[nx][ny]):
                if (grid[nx][ny] == 'R' or grid[nx][ny] == 'G') and color == "RG":
                    q.append((nx, ny))
                    visited[nx][ny] = True
                elif grid[nx][ny] == color:
                    q.append((nx, ny))
                    visited[nx][ny] = True


#BFS
count = 0
for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            count += 1
            BFS((x, y), grid[x][y])
print(count, end=' ')

visited = [[False for x in range(N)] for y in range(N)]
count = 0

#BFS_RG
for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            count += 1
            BFS_RG((x, y), grid[x][y])
print(count, end=' ')