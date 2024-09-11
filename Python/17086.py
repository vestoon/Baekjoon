import sys
import collections
input = sys.stdin.readline

# d = (-1, 0, 1)
dy = (0, 0, 1, 1, 1, -1, -1, -1)
dx = (1, -1, 0, 1, -1, 0, 1, -1)

def bfs(i, j):
    visited = [[False for x in range(M)] for y in range(N)]
    q = collections.deque()
    q.append((i, j))
    visited[i][j] = True
    distance = 0

    while q:
        l = len(q)
        for _ in range(l):
            y, x = q.popleft()
            if space[y][x] == 1:
                return distance

            # for dx in d:
            #     for dy in d:
            #         if dx or dy:
            #             ny, nx = y + dy, x + dx
            #             if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            #                 visited[ny][nx] = True
            #                 q.append((ny, nx))

            for n in range(8):
                ny, nx = y + dy[n], x + dx[n]
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))


        distance += 1


N, M = map(int, input().split())
space = [list(map(int, input().split())) for x in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        if space[i][j]:
            continue

        ans = max(ans, bfs(i, j))
        # print(i, j, ans)

print(ans)

"""
4 4
0 0 0 0
0 0 0 0
0 0 0 0
1 0 0 0
"""