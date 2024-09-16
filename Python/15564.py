import sys
import math
sys.setrecursionlimit(100100)
input =sys.stdin.readline

N, Q = map(int, input().split())
inp = list(map(int, input().split()))
maxH = int(math.log2(N)+2)+1

adj_list = [[] for x in range(N+1)]
parent = [[0 for x in range(maxH)] for y in range(N+1)] # 2**j-th parent of i (dp for LCA)
depth = [-1 for x in range(N+1)]
parent_cent = [0 for x in range(N+1)] # parent in centroid tree
isCentroid = [False for x in range(N+1)] # if node is set to centroid
isCentroid[0] = True
sz = [0 for x in range(N+1)] # size of subtree
violin_dist = [-1 for x in range(N+1)] # min dist to violin in the centroid tree of x
# cache = {}

for i in range(N-1):
    adj_list[i+2].append(inp[i])
    adj_list[inp[i]].append(i+2)


# dfs(1, 0)
def dfs(cur:int, prev:int): # initialize depth and Perform dp for LCA
    depth[cur] = depth[prev]+1
    parent[cur][0] = prev

    for i in range(1, maxH):
        parent[cur][i] = parent[parent[cur][i-1]][i-1]
    
    for nxt in adj_list[cur]:
        if nxt == prev: continue
        dfs(nxt, cur)


def LCA(a:int, b:int) -> int:
    target = a if depth[a] < depth[b] else b 
    cmp = b if depth[a] < depth[b] else a # cmp is usually deeper than target

    # make depth same
    if depth[target] != depth[cmp]:
        for i in range(maxH-1, -1, -1):
            if depth[parent[cmp][i]] >= depth[target]:
                cmp = parent[cmp][i]
    
    # find LCA
    if target != cmp:
        for i in range(maxH-1, -1, -1):
            if parent[cmp][i] != parent[target][i]:
                cmp, target = parent[cmp][i], parent[target][i]
        return parent[cmp][0]
    return target 


def dist(a:int, b:int) -> int:
    return depth[a] + depth[b] -2*depth[LCA(a, b)]


# def dist_cache(a:int, b:int) ->int:
#     if (a, b) in cache:
#         return cache[(a, b)]
#     if (b, a) in cache:
#         return cache[(b, a)]
#     d = dist(a, b)
#     cache[(a, b)] = d
#     return d


def getSize(cur:int, prev:int) -> int: # return size of subtree of cur node and set size of subtree of descendant node
    sz[cur] = 1

    for nxt in adj_list[cur]:
        if isCentroid[nxt] or nxt == prev:
            continue

        sz[cur] += getSize(nxt, cur)        


    return sz[cur]


def findCent(cur:int, prev:int, totalSize:int) -> int: # find centroid node of subtree containing cur node
    for nxt in adj_list[cur]:
        if isCentroid[nxt] or nxt == prev: continue
        if sz[nxt] > totalSize//2: # sz는 고정된 값이 아니다, 탐색 상황에 따라서 달라질 수 있다.
            return findCent(nxt, cur, totalSize)
    return cur


# centroidDecomp(1, 0)
def centroidDecomp(cur:int, prev:int):
    totalSize = getSize(cur, prev)
    cent = findCent(cur, prev, totalSize) # 0이어도 되지 않나 왜 -1 로 했을까 -> 일단 0으로 바꿔둠
    # print("cent", cent)
    isCentroid[cent] = True
    parent_cent[cent] = prev
    
    for nxt in adj_list[cent]:
        if isCentroid[nxt] or nxt == prev:
            continue
        centroidDecomp(nxt, cent)


dfs(1, 0)
centroidDecomp(1, 0)
for _ in range(Q):
    cmd, x = map(int, input().split())
    if cmd == 1:
        violin_dist[x] = 0
        p = parent_cent[x]
        while p:
            d = dist(x, p)
            if violin_dist[p] == -1 or d < violin_dist[p]:
                violin_dist[p] = dist(x, p)
            p = parent_cent[p]
    else:
        ans = -1
        p = x
        while True:
            if violin_dist[p] != -1:
                if ans == -1:
                    ans = dist(x, p) + violin_dist[p]
                else:
                    ans = min(ans, dist(x, p) + violin_dist[p])
            p = parent_cent[p]
            if not p:
                break
        print(ans)
