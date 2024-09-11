# DFS
# Must use adjacent_list
import sys
sys.setrecursionlimit(200010)
input = sys.stdin.readline


def dfs(n):
    visited[n] = True
    ret = 1

    for nxt in forest[n]:
        if visited[nxt]:
            continue

        ret += dfs(nxt)

    return ret


ans = 1
N, M = map(int, input().split())
forest = [[] for y in range(N+1)]
visited = [False for x in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    forest[u].append(v)
    forest[v].append(u)

for n in range(1, N+1):
    if not visited[n]:
        ans *= dfs(n)
        ans %= 1000000007

print(ans)