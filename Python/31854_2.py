import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
adj_list = [[] for x in range(N**2)]
in_degree = [0 for x in range(N**2)]
ans = [0 for x in range(N**2)]
order_que = deque()

for i in range(N):
    line = input().rstrip().split()
    for j in range(N-1):
        if line[j] == '>':
            adj_list[i*N + j].append(i*N + j+1)
            in_degree[i*N + j+1] += 1
        else:
            adj_list[i*N + j+1].append(i*N + j)
            in_degree[i*N + j] += 1

for i in range(N-1):
    line = input().rstrip().split()
    for j in range(N):
        if line[j] == '>':
            adj_list[i*N + j].append((i+1)*N + j)
            in_degree[(i+1)*N + j] += 1
        else:
            adj_list[(i+1)*N + j].append(i*N + j)
            in_degree[i*N + j] += 1

for x in range(N**2):
    if not in_degree[x]:
        order_que.append(x)

cur_order = N**2
while order_que:
    cur = order_que.popleft()
    ans[cur] = cur_order
    cur_order -= 1

    for nxt in adj_list[cur]:
        in_degree[nxt] -= 1
        if not in_degree[nxt]:
            order_que.append(nxt)

for i in range(N):
    for j in range(N):
        print(ans[i*N + j], end=' ')
    print()



