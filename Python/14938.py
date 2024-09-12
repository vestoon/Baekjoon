import sys
import heapq
input = sys.stdin.readline

INF = 1501

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
adj_list = [[INF for x in range(n+1)]for y in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    adj_list[a][b] = l
    adj_list[b][a] = l

ans = 0
for src in range(1, n+1):
    item = items[src]
    distance = [INF for x in range(n+1)]
    visited = [False for x in range(n+1)]
    visited[src] = True
    distance[src] = 0
    pq = [(0, src)]  # (distance, node)
    while pq:
        d, cur = heapq.heappop(pq)
        for nxt in range(1, n+1):
            w = adj_list[cur][nxt]
            if w != INF and d + w < distance[nxt] and w + d <= m:
                distance[nxt] = d + w
                heapq.heappush(pq, (d+w, nxt))
                if not visited[nxt]:
                    item += items[nxt]
                    visited[nxt] = True

    ans = max(ans, item)

print(ans)

"""
4 5 4
1 2 3 4 
1 2 5
1 3 1
2 3 2
2 4 1
"""