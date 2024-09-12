import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())

adj_list = [[] for x in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj_list[u].append((w, v))

src, dst = map(int, input().split())


def search(u, v):
    distance = [[INF, []] for x in range(N+1)]  # distance, path
    distance[u] = [0, [u]]
    que = [(0, u)]

    while que:
        d, cur = heapq.heappop(que)
        if d < distance[cur][0]:
            continue
        if cur == v:
            return distance[v]

        for nd, nxt in adj_list[cur]:
            if nd+d >= distance[nxt][0]:
                continue
            distance[nxt] = [nd+d, distance[cur][1]+[nxt]]
            heapq.heappush(que, (nd+d, nxt))


print(search(src, dst)[0])
