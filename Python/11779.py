import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

adj_mat = [[1000001 for y in range(n+1)] for x in range(n+1)]
distance = [[] for x in range(n+1)]

for _ in range(m):
    src, dst, weight = map(int, input().split())
    adj_mat[src][dst] = min(adj_mat[src][dst], weight)

s, d = map(int, input().split())
distance[s] = [0, s]
pq = [(0, s)]

while pq:
    front = heapq.heappop(pq)

    w, cur = front
    for nxt in range(1, n+1):
        if adj_mat[cur][nxt] == 1000001:
            continue

        if (not distance[nxt]) or w + adj_mat[cur][nxt] < distance[nxt][0]:
            distance[nxt] = [w + adj_mat[cur][nxt]] + distance[cur][1:] + [nxt]
            pq.append((w + adj_mat[cur][nxt], nxt))

print(distance[d][0])
print(len(distance[d])-1)
print(*distance[d][1:])
