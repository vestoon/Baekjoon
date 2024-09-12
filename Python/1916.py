import sys
import heapq
input = sys.stdin.readline
INF = int(1e8)

N = int(input())
M = int(input())

adjMat = [[] for y in range(N+1)]
for _ in range(M):
    s, d, w = map(int, input().split())
    adjMat[s].append((w, d))  # (w, d)

A, B = map(int, input().split())  # 찾고자 하는 시작 지점


def dijkstra(src, dst):
    distance = [INF for x in range(N+1)]
    distance[src] = 0
    hq = [(0, src)]  # (distance, vertex)
    while hq:
        d, front = heapq.heappop(hq)
        if distance[front] != d:
            continue

        for nd, nxt in adjMat[front]:
            if d + nd < distance[nxt]:
                distance[nxt] = d + nd
                # print(distance)
                heapq.heappush(hq, (d + nd, nxt))

    return distance[dst]


print(dijkstra(A, B))


