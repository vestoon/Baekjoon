import queue
import sys
import collections
M, N = map(int, sys.stdin.readline().split())  # M: 가로, N: 세로

warehouse = []
ripe_tomatoes = []
q = queue.Queue()  # 익은 토마토들 좌표
# visited = [[0]*M]*N
for r in range(N):  # 1: 익은 토마토, 0: 안익은 토마토, -1: 토마토 없음
    rowInp = list(map(int, sys.stdin.readline().split()))
    warehouse.append(rowInp)

    for ti in range(M):
        if rowInp[ti] == 1:
            q.put((r, ti))
q.put(0)

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

days = 1
while q.qsize() != 0:
    front = q.get()
    if front:
        # print("front:", front)
        for i in range(4):
            sur = (front[0]+dx[i], front[1]+dy[i])
            # print("sur:", sur)
            if 0 <= sur[0] < N and 0 <= sur[1] < M and warehouse[sur[0]][sur[1]] == 0:
                warehouse[sur[0]][sur[1]] = days + 1
                q.put(sur)
        # for g in warehouse:
        #     print(g)
        # print()
    elif q.qsize():
        # print('days++')
        days += 1
        q.put(0)

for i in range(N):
    for j in range(M):
        if warehouse[i][j] == 0:
            print(-1)
            exit()

print(days-1)