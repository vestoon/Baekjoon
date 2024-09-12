import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().split())  # M: 가로, N: 세로, H: 높이
warehouse = []
ripe_tomato = deque()

# 1: 익은 토마토, 0: 안익은 토마토, -1: 토마토 없음
count = 0  # 안익은 토마토의 개수
for z in range(H):
    floor = []
    for y in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        for x in range(M):
            if line[x] == 1:
                ripe_tomato.append((z, y, x))
            elif line[x] == 0:
                count += 1
        floor.append(line)

    warehouse.append(floor)
# print("initial count:", count)
dz = (1, -1, 0, 0, 0, 0)
dy = (0, 0, -1, 1, 0, 0)
dx = (0, 0, 0, 0, -1, 1)
ripe_tomato.append(0)
days = 0

while ripe_tomato:
    cur = ripe_tomato.popleft()
    if cur:
        for s in range(6):
            # sur = (cur[0]+dz[s], cur[1]+dy[s], cur[2]+dx[s])
            z, y, x = cur[0]+dz[s], cur[1]+dy[s], cur[2]+dx[s]
            # print("sur:", z, y, x)
            if 0 <= z < H and 0 <= y < N and 0 <= x < M and warehouse[z][y][x] == 0:
                warehouse[z][y][x] = 1
                count -= 1
                # print("count:", count)
                ripe_tomato.append((z, y, x))
    elif ripe_tomato:

        # for f in warehouse:
        #     for l in f:
        #         print(l)
        #     print()
        # print('next')
        days += 1
        ripe_tomato.append(0)

# #  warehouse 상태 확인
# for f in warehouse:
#     for l in f:
#         print(l)
#     print()

# for i in warehouse:
#     for j in i:
#         for k in j:
#             if k == 0:
#                 print(-1)
#                 exit()

# print("count:", count)
if count:
    print(-1)
else:
    print(days)

