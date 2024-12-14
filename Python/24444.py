import sys
from collections import deque
input = sys.stdin.readline

N, M, R= map(int, input().split())
adj_list = [[] for x in range(N+1)]
order = [0 for x in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

for n in range(N+1):
    adj_list[n].sort()

que = deque()
que.append(R)
order[R] = 1
cnt = 1

while que:
    cur = que.popleft()

    for nxt in adj_list[cur]:
        if not order[nxt]:
            que.append(nxt)
            order[nxt] = cnt+1
            cnt += 1

for i in range(1, N+1):
    print(order[i])