import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
dist = [sys.maxsize for x in range(N+1)]
adj_list = [[] for x in range(N+1)]
visited = [False for x in range(N+1)]
pq = [(0, 1)]
ans = 0
cnt = 0
maxEdge = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    adj_list[A].append((C, B))
    adj_list[B].append((C, A))


while cnt != N:
    d, cur = heapq.heappop(pq)
    if visited[cur]: continue
    
    cnt += 1
    ans += d
    maxEdge = max(maxEdge, d)
    visited[cur] = True

    for nd , nxt in adj_list[cur]:
        if nd < dist[nxt]:
            dist[nxt] = nd
            heapq.heappush(pq, (nd, nxt))

print(ans - maxEdge)
