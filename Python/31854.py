import sys
sys.setrecursionlimit(2000000)
input = sys.stdin.readline
# DFS로 위상 정렬하기


N = int(input())

adj_list = [[] for x in range(N**2)]
visited = [False for x in range(N**2)]
ans = [0 for x in range(N**2)]
# i, j -> i*N + j

# 좌우 
for i in range(N):
    line = input().rstrip().split()
    for j in range(N-1):
        # (i,j) cmp (i,j+1)
        if line[j] == '<':
            adj_list[i*N + j+1].append(i*N+j)
        else:
            adj_list[i*N+j].append(i*N + j+1)
            
# 상하
for i in range(N-1):
    line = input().rstrip().split()
    for j in range(N):
        if line[j] == '<':
            adj_list[(i+1)*N+j].append(i*N+j)
        else:
            adj_list[i*N+j].append((i+1)*N+j)


def dfs(cur: int):
    global top_order
    # print('cur', cur)
    visited[cur] = True

    for nxt in adj_list[cur]:
        if not visited[nxt]:
            dfs(nxt)

    ans[cur] = top_order
    top_order += 1


top_order = 1
for x in range(N**2):
    if not visited[x]:
        dfs(x)

for i in range(N):
    for j in range(N):
        print(ans[i*N+j], end=' ')
    print()
