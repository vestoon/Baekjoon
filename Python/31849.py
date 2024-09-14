import sys
input = sys.stdin.readline
from collections import deque
INF = 2100
ans = INF*100
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

N, M, R, C = map(int, input().split())
distance = [[INF for x in range(M)] for y in range(N)]
# 편의점 기준으로 bfs 돌리면서 거리 저장

houses = []
for _ in range(R):
    a, b, p = map(int, input().split())
    houses.append((a, b, p))

q = deque()
for _ in range(C):
    c, d = map(int, input().split())
    c -= 1; d -= 1
    distance[c][d] = 0
    q.append((c, d))

while q:
    i, j = q.popleft() 
    cd = distance[i][j]

    for k in range(4):
        ni, nj = i+dy[k], j+dx[k]
        if 0<=ni<N and 0<=nj<M and cd+1 < distance[ni][nj]:
            distance[ni][nj] = cd+1
            q.append((ni, nj))


for a, b, p in houses:
    ans = min(ans, p*distance[a-1][b-1])

# for _ in distance:
#     print(*_)
print(ans)