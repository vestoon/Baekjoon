import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
src = int(sys.stdin.readline())
adjList = [[] for x in range(V+1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    adjList[u].append((v, w))

INF = sys.maxsize
distance = [INF for x in range(V+1)]
visited = [False for x in range(V+1)]
distance[src] = 0
hq = []

for _ in range(V):
    cur = 0
    # 최소 거리를 가지는 cur 찾기
    for vertex in range(1, V+1):
        if visited[vertex]:
            continue

        if distance[vertex] < distance[cur]:
            cur = vertex
    visited[cur] = True

    for nxt in adjList[cur]:
        # 방문하지 않았어야 함, 애초애 갈 수 있는 정점이어야 함
        nxt, w = nxt
        distance[nxt] = min(distance[nxt], distance[cur] + w)

for x in range(1, V+1):
    if distance[x] == sys.maxsize:
        print("INF")
    else:
        print(distance[x])

# print(sys.getsizeof(INF))
#
#
# t_distance = [20000*300000 for x in range(20001)]
# z_distance = [0 for x in range(20001)]
# t_visited = [True for x in range(20001)]
# t_adjMat = [[10 for x in range(20001)] for y in range(20001)]
#
# print(sys.getsizeof(t_distance))
# print(sys.getsizeof(z_distance))
# print(sys.getsizeof(t_visited))
# print(sys.getsizeof(t_adjMat))
#
