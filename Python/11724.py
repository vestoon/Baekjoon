import sys
sys.setrecursionlimit(2000)
N, M = map(int, sys.stdin.readline().split())  # N: 정점의 개수, M: 간선의 개수
adjacent_list = {x: [] for x in range(1, N+1)}
visited = [False for x in range(N+1)]
count = 0

for e in range(M):
    i, j = map(int, sys.stdin.readline().split())
    adjacent_list[i].append(j)
    adjacent_list[j].append(i)


def DFS(n):
    visited[n] = True
    for nxt in adjacent_list[n]:
        if not visited[nxt]:
            DFS(nxt)


for st_vertex in range(1, N+1):
    if not visited[st_vertex]:
        count += 1
        DFS(st_vertex)

print(count)
