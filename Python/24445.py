import sys
import collections
input = sys.stdin.readline

N, M, R = map(int, input().split())
adj_list = [[] for x in range(N+1)]
visit_order = [0 for x in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

for node in adj_list:
    node.sort(reverse=True)

que = collections.deque()
que.append(R)
visit_order[R] = 1
cur_order = 1

while que:
    cur = que.popleft()

    for nxt in adj_list[cur]:
        if not visit_order[nxt]:
            que.append(nxt)
            visit_order[nxt] = cur_order+1
            cur_order += 1

for i in range(1, N+1):
    print(visit_order[i])