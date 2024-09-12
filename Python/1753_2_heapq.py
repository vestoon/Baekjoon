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
distance[src] = 0
hq = []

heapq.heappush(hq, (0, src))

while hq:
    base, cur = heapq.heappop(hq)
    if distance[cur] != base:
        continue

    for nxt, w in adjList[cur]:
        if base + w < distance[nxt]:
            distance[nxt] = base + w
            heapq.heappush(hq, (distance[nxt], nxt))

for x in range(1, V+1):
    if distance[x] == sys.maxsize:
        print("INF")
    else:
        print(distance[x])

