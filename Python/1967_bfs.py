import sys
import heapq
import collections
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())

adj_list = {x: [] for x in range(1, n+1)}  # (weight, destination)
for _ in range(n-1):
    s, d, w = map(int, input().split())
    adj_list[s].append((w, d))
    adj_list[d].append((w, s))


def bfs(root):
    distance = [[INF, x] for x in range(n+1)]
    distance[0] = [0, 0]
    distance[root] = [0, root]
    hq = [(0, root)]
    while hq:
        d, cur = heapq.heappop(hq)
        if d != distance[cur][0]:
            continue

        for nd, nxt in adj_list[cur]:
            if distance[cur][0] + nd < distance[nxt][0]:
                distance[nxt][0] = distance[cur][0] + nd
                heapq.heappush(hq, tuple(distance[nxt]))

    # print(distance)
    return max(distance)


u = bfs(1)[1]
print(bfs(u)[0])
