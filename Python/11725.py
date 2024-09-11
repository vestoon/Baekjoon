import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
adj_list = {x: [] for x in range(1, N+1)}
parent = [0 for x in range(N+1)]
parent[1] = 1
for _ in range(N-1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


def dfs(vertex):

    for nxt in adj_list[vertex]:
        if not parent[nxt]:
            parent[nxt] = vertex
            dfs(nxt)


dfs(1)
for x in parent[2:]:
    print(x)
