import sys
import collections
input = sys.stdin.readline

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

"""
두 바이러스 사이의 모든 경계가 3번 바이러스가 되는 것은 아니다.
동시에 감염돼야 한다. 
"""

def bfs_1cycle(que:collections.deque, mode):
    if not que: return
    l = len(que)
    for _ in range(l):
        i, j = que.popleft()
        if village[i][j] == 3: continue

        for d in range(4):
            ni, nj = i+dx[d], j+dy[d]

            if ni<0 or nj<0 or N<=ni or M<=nj: continue
            nxt = village[ni][nj]# -1, 0, 1, 2, 3

            if nxt == 0: # 아무 것도 감염되지 않은 빈 공간
                village[ni][nj] = mode
                cnt_virus[mode] += 1
                distance[ni][nj] = cur_distance
                que.append((ni, nj))
            elif nxt == 3-mode and distance[ni][nj] == cur_distance: # 다른 바이러스가 이미 감염된 경우
                village[ni][nj] = 3
                cnt_virus[3] += 1
                cnt_virus[3-mode] -= 1

            


N, M = map(int, input().split())
village = []
distance = [[sys.maxsize for x in range(M)] for y in range(N)]
virus1, virus2 = (0, 0), (0, 0)
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 1:
            virus1 = (i, j)
        elif line[j] == 2:
            virus2 = (i, j)
    village.append(line)
cnt_virus = [0, 1, 1, 0] # 바이러스 종류별 감염된 마을 수, 1~3
que1, que2 = collections.deque([virus1]), collections.deque([virus2])

cur_distance = 0
while que1 or que2:
    cur_distance += 1
    bfs_1cycle(que1, 1)
    # for z in village:
    #     print(*z)
    # print()
    bfs_1cycle(que2, 2)
    # for z in village:
    #     print(*z)
    # print('-')

print(*cnt_virus[1:])
