import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
adj_list = [[] for x in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())   
    adj_list[B].append(A)

def bfs(src:int) -> int:
    visited = [False for x in range(N+1)]
    visited[src] = True
    que = deque([src])
    ret = 1

    while que:
        cur = que.popleft()

        for nxt in adj_list[cur]:
            if not visited[nxt]:
                ret += 1
                visited[nxt] = True
                que.append(nxt)
    
    return ret


ans_list = []
ans = 0
for i in range(1, N+1):
    cnt = bfs(i)
    if ans < cnt:
        ans = cnt
        ans_list = [i]
    elif ans == cnt:
        ans_list.append(i)

print(*ans_list)