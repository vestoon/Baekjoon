import sys
import collections
# N: 정점의 수 , E: 간선의 수
N, E = map(int, sys.stdin.readline().split())
adMa = [[0 for x in range(N+1)] for y in range(N+1)]

# 인접 행렬 초기화
for _ in range(E):
    # a와 b  사의의 거리가 c 이다
    a, b, c = map(int, sys.stdin.readline().split())
    adMa[a][b] = c
    adMa[b][a] = c

# 반드시 거쳐가야 하는 두 점
v1, v2 = map(int, sys.stdin.readline().split())
iMax = 200000001


# i에서 j 로 가는 최단거리 탐색
def DISearch(i, j):
    distance = [iMax for x in range(N+1)]
    distance[i] = 0
    # (vertex, distance)
    q = collections.deque()
    q.append((i, 0))
    while len(q):
        front, d = q.popleft()
        # print(front, d)
        for nxt in range(1, N+1):
            if adMa[front][nxt] and d + adMa[front][nxt] < distance[nxt]:
                q.append((nxt, d + adMa[front][nxt]))
                distance[nxt] = d + adMa[front][nxt]

    return distance[j] if distance[i] != iMax else -1


mid = DISearch(v1, v2)
ans = mid + min(DISearch(1, v1) + DISearch(v2, N), DISearch(1, v2) + DISearch(v1, N))

if ans >= iMax:
    print(-1)
else:
    print(ans)
