import sys
import collections
N, M = map(int, sys.stdin.readline().split())
campus = []
visited = [[False for x in range(M)] for y in range(N)]

count = 0  # 발견한 친구의 명수

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

src = False
for x in range(N):
    line = list(sys.stdin.readline())[:-1]
    if not src:
        for y in range(M):
            if line[y] == 'I':
                src = (x, y)
                break

    campus.append(line)

# src 에서부터 bfs
q = collections.deque()
q.append(src)
visited[src[0]][src[1]] = True

while q:
    i, j = q.popleft()  # front
    # print('front', i, j)

    for n in range(4):
        ni, nj = i + dx[n], j + dy[n]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            if campus[ni][nj] == 'X':
                continue
            q.append((ni, nj))
            visited[ni][nj] = True
            if campus[ni][nj] == 'P':
                count += 1


if count:
    print(count)
else:
    print("TT")



