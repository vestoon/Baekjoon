import sys
import heapq
# N: 마을의 개수, M: 간선의 개수, X: 파티 장소
N, M, X = map(int, sys.stdin.readline().split())

# 인접 행렬 생성
adjacent_list = {x: [] for x in range(1, N+1)}  # (nxt, weight)
for _ in range(M):
    src, dst, weight = map(int, sys.stdin.readline().split())
    adjacent_list[src].append((dst, weight))

M = 0
for vertex in range(1, N+1):
    if vertex == X:
        continue
    v_to = [int(1e9) for _ in range(N+1)]
    X_to = [int(1e9) for _ in range(N+1)]
    q = []
    heapq.heappush(q, (0, vertex))  # (vertex, acc)
    while q:
        acc, front = heapq.heappop(q)
        for nxt, w in adjacent_list[front]:
            nw = acc + w
            if v_to[nxt] > nw:
                v_to[nxt] = nw
                heapq.heappush(q, (nw, nxt))

    heapq.heappush(q, (0, X))  # (vertex, acc)
    while q:
        acc, front = heapq.heappop(q)
        for nxt, w in adjacent_list[front]:
            nw = acc + w
            if X_to[nxt] > nw:
                X_to[nxt] = nw
                heapq.heappush(q, (nw, nxt))

    M = max(v_to[X] + X_to[vertex], M)

print(M)

