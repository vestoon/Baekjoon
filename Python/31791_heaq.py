import sys
import heapq
input = sys.stdin.readline

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

N, M = map(int, input().split())
Tg, Tb, X, B = map(int, input().split())

grid = []
spread_time = [[Tg+1 for x in range(M)] for y in range(N)]
viruses = []

for i in range(N):
    line = list(input().rstrip())
    for j in range(M):
        if line[j] == '*':
            heapq.heappush(viruses, (0, i, j))
            # spread_time[i][j] = 0
    grid.append(line)

while viruses:
    w, i, j = heapq.heappop(viruses)
    if spread_time[i][j] <= w: continue
    spread_time[i][j] = w

    for d in range(4):
        ni, nj = i+dx[d], j+dy[d]
        if ni<0 or nj<0 or N<=ni or M<=nj: continue
        t = w + (1 + Tb if grid[ni][nj] == '#' else 1)
        if spread_time[ni][nj] <= t: continue

        # spread_time[ni][nj] = t
        heapq.heappush(viruses, (t, ni, nj))

    # for k in spread_time:
    #     print(*k)
    # print()

exsist = False
for i in range(N):
    for j in range(M):
        if Tg < spread_time[i][j]:
            exsist = True
            print(i+1, j+1)
if not exsist:
    print(-1)