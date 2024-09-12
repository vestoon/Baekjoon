import sys
import collections

V, E = map(int, sys.stdin.readline().split())
src = int(sys.stdin.readline())
adjMat = [[0 for x in range(V+1)] for y in range(V+1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    adjMat[u][v] = w

INF = 20000*300000
distance = [INF for x in range(V+1)]
distance[src] = 0

dq = collections.deque()
dq.append(src)
while len(dq):
    # print(dq)
    front = dq.popleft()
    for nxt in range(1, V+1):
        if not adjMat[front][nxt]:
            continue
        if distance[nxt] > distance[front] + adjMat[front][nxt]:
            distance[nxt] = distance[front] + adjMat[front][nxt]
            dq.append(nxt)

for x in range(1, V+1):
    if distance[x] == INF:
        print("INF")
    else:
        print(distance[x])

# test_distance = [INF for x in range(20001)]
# print(sys.getsizeof(test_distance))
#
# test_adjMat = [[10 for x in range(20001)] for y in range(20001)]
# print(sys.getsizeof(test_adjMat))
#
# test_dq = collections.deque()
# for x in range(1, 20001):
#     dq.append(INF)
# # print(dq)
# print(sys.getsizeof(test_dq))

