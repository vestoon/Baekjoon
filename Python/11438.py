import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

N = int(input())
adj_list = [[] for x in range(N+1)]
depth = [0 for x in range(N+1)]
# parent = [0 for x in range(N+1)]
# dp[i][j] : 2^j th parent of node i
dp = [[0 for x in range(20)] for y in range(N+1)] # set size 20

for _ in range(N-1):
    # print(map(int, input().split()))
    # exit()
    u, v = map(int, input().split())

    adj_list[u].append(v)
    adj_list[v].append(u)


def dfs(cur:int, prev:int ): # set depth and perform dp for LCA
    depth[cur] = depth[prev]+1
    dp[cur][0] = prev

    for i in range(1, 20):
        dp[cur][i] = dp[dp[cur][i-1]][i-1]

    for nxt in adj_list[cur]:
        if nxt == prev:
            continue
        dfs(nxt, cur)


def LCA(x:int, y:int) ->int:
    l = x if depth[x] > depth[y] else y # lower 
    u = y if depth[x] > depth[y] else x # upper

    # make lower & upper's depth same
    if depth[l] != depth[u]:
        for i in range(19, -1, -1):
            if depth[dp[l][i]] >= depth[u]:
                l = dp[l][i]
    # print("step1", l, u, dp[l][0])
    
    # find LCA at the same depth
    if l != u:
        for i in range(19, -1, -1):
            if dp[l][i] != dp[u][i]:
                l, u = dp[l][i], dp[u][i]
        return dp[l][0]
        # l = dp[l][0]
    return l


dfs(1, 0)

M = int(input())
for _ in range(M):
    u, v = map(int, input().split())
    print(LCA(u, v))