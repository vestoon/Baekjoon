import sys
import collections

N, M = map(int, sys.stdin.readline().split())
paper = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    paper.append(line)

visited = [[False for x in range(M)] for y in range(N)]
dx = (1, 0)
dy = (0, 1)
# dx = (1,-1, 0, 0)
# dy = (0, 0, 1, -1)
ans = 0


def search(path, acc):
    x, y = path[-1]
    visited[x][y] = True
    if len(path) == 4:
        global ans
        if acc > ans:
            ans = acc
        visited[x][y] = False
        return
    # path 가 완성되지 않은 경우
    # 종이의 범위를 제한해 보자
    src = path[0]
    for cor in path:
        for n in range(2):
            nx, ny = cor[0] + dx[n], cor[1] + dy[n]
            if src[0] <= nx < N and src[1] <= ny < M and not visited[nx][ny]:
                search(path + [(nx, ny)], acc + paper[nx][ny])
    visited[x][y] = False


ans = 0
for i in range(N):
    for j in range(M):
        # print('src:', i, j)
        # for _ in visited:
        #   print(_)
        search([(i, j)], paper[i][j])

print(ans)
