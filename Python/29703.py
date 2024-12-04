import sys
from collections import deque
import heapq
input = sys.stdin.readline

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

"""
현재 위치에서 먹이가 있는 곳들 중 하나를 방문했다가 집으로 돌아가는 최단 거리를 구하는 문제

현재 위치에서 bfs로 먹이가 있는 모든 곳들에 대한 최단 경로를 구한 뒤에 멀티 소스 bfs를 다시 수행?
어차피 먹이가 있는 위치 방문해야 하니까 방문 배열을 만드는게 좋을듯
"""

N, M = map(int, input().split()) # N: 세로 , M: 가로
village = []
start = ()
home = ()
distance1 = [[sys.maxsize for x in range(M)] for y in range(N)]
distance2 = [[sys.maxsize for x in range(M)] for y in range(N)]
que1 = deque() # 현재 위치에서 물고기까지의 거리를 찾는 큐

def bfs1(que1) -> list:
    que2 = []
    while que1:
        i, j = que1.popleft()

        for d in range(4):
            ni, nj = i+dx[d], j+dy[d]
            if 0<=ni<N and 0<=nj<M and distance1[i][j] + 1 < distance1[ni][nj] and village[ni][nj] != 'D':
                distance1[ni][nj] = distance1[i][j]+1
                que1.append((ni, nj))

                if village[ni][nj] == 'F':
                    # print(distance1[ni][nj])
                    distance2[ni][nj] = distance1[ni][nj]
                    heapq.heappush(que2, (distance2[ni][nj], ni, nj))
    return que2

def bfs2(que2):

    while que2:
        d, i, j = heapq.heappop(que2)
        if distance2[i][j] < d: continue

        for d in range(4):
            ni, nj = i+dx[d], j+dy[d]
            if 0<=ni<N and 0<=nj<M and distance2[i][j]+1 < distance2[ni][nj] and village[ni][nj] != 'D':
                distance2[ni][nj] = distance2[i][j]+1
                heapq.heappush(que2, (distance2[ni][nj], ni, nj))
                
                if village[ni][nj] == 'H':
                    return distance2[ni][nj]
                
    return -1


for i in range(N):
    line = input().rstrip()
    for j in range(M):
        if line[j] == 'S':
            distance1[i][j] = 0
            que1.append((i, j))


    village.append(line)

que2 = bfs1(que1)
print(bfs2(que2))



