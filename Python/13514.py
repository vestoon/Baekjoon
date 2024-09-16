import sys
import heapq
sys.setrecursionlimit(101010)
input  = sys.stdin.readline

"""
문제점)
 주어진 지점의 모든 조상 노드에서 흰색까지의 거리를 저장 후 최소값 을 찾기에는
조상 노드의 개수가 n개까지 갈 수 있기 때문에 TLE가 생긴다. 

해결 방안)
 Centroid Decomposition을 통해서 조상 노드의 수를 줄여 보자

필요한 것)
- Centroid Tree의 모든 조상 노드에서 흰색까지의 최단거리를 저장할 수 있어야 한다
(이 문제의 경우에는 흰색이 사라질 수도 있기 때문에 우선순위 큐로 관리해야 함)
-> 흰색이 생길 때마다 Centroid 상의 모든 조상에 LCA를 이용하여 자신의 거리를 큐에 넣어야 함

- LCA를 계산하기 위한 2차원 dp table 필요: N * log(N)
- 각 정점에서 관리하는 최단거리르 저장하기 위한 우선순위 큐(HeapQueue) 필요 : N * ?
- 색깔을 저장하는 배열을 따로 만들고 최단 거리를 뽑을 때 색이 맞지 않으면 다시 뽑는다


두 정점(a, b) 사이의 거리 구하기: a 깊이 + b 깊이 -2LCA의 깊이

1. 일단 Centroid Tree를 만든다
2. 
"""


N = int(input())
adj_list = [[] for x in range((N+1))]
depth = [0 for x in range(N+1)] # depth of node in orginal tree
sz = [0 for x in range(N+1)] # size of subtree
centroid = [0 for x in range(N+1)] # parent of node in centroid tree
isCentroid = [False for x in range(N+1)] # Whether node is set to centroid 
color = [False for x in range(N+1)] # True if node's color is white
parent = [[0 for x in range(20)] for y in range(N+1)] # parent[i][j] := 2*j th parent of node i
# heapqs for storing shortest path
shortest = [[] for x in range(N+1)] # element format: (distance, node)


def dfs(cur: int, prev: int): # store depth & dp
    depth[cur] = depth[prev]+1
    parent[cur][0] = prev

    for i in range(1, 20): # LCA
        parent[cur][i] = parent[parent[cur][i-1]][i-1]

    for nxt in adj_list[cur]:
        if nxt == prev:
            continue
        dfs(nxt, cur)


def LCA(a: int , b:int) -> int:
    if depth[a] < depth[b]: # Make a lower than b
        a, b = b, a
    
    # Make depth same
    if depth[a] != depth[b]:
        for i in range(19, -1, -1):
            if depth[parent[a][i]] >= depth[b]:
                a = parent[a][i]
    
    # Find LCA
    if a != b:
        for i in range(19, -1, -1):
            if parent[a][i] != parent[b][i]:
                a, b = parent[a][i], parent[b][i]
        return parent[a][0]
    return a


def dist(a:int, b:int) -> int:
    return depth[a] + depth[b] - 2*depth[LCA(a, b)]


def getSize(cur: int, prev:int) ->int:
    sz[cur] = 1
    for nxt in adj_list[cur]:
        if nxt == prev or isCentroid[nxt]:
            continue
        sz[cur] += getSize(nxt, cur)
    
    return sz[cur]
        

# Find Centroid node
def findCent(cur:int, prev:int, totalSize) -> int:
    for nxt in adj_list[cur]:
        if isCentroid[nxt] or nxt == prev: # subtree의 사이즈가 절반 이상일 때 호출되므로 그
            continue                       # 그 이전 subtree는 절반 이하라 가정, 아마 탐색 순서가 일정해야 할듯
        if sz[nxt] > totalSize//2:
            return findCent(nxt, cur, totalSize)
    return cur

# Centroid Decomposing in subtree containg cur node
def centroidDecomp(cur:int, prev:int):
    totalSize = getSize(cur, prev)
    cent = findCent(cur, prev, totalSize)
    isCentroid[cent] = True
    centroid[cent] = prev # At first search, prev is 0
    for nxt in adj_list[cent]:
        if (isCentroid[nxt] or nxt == prev):
            continue
        centroidDecomp(nxt, cent)
    

def update(x:int):
    color[x] = False if color[x] else True
    if not color[x]: return

    cur = x
    while cur:
        heapq.heappush(shortest[cur], (dist(cur, x), x))
        cur = centroid[cur]


def query2(x:int) -> int:
    ret = sys.maxsize

    cur = x # current searching node
    while cur:
        while shortest[cur]:
            front = shortest[cur][0]
            if color[front[1]]:
                ret = min(ret, front[0] + dist(cur, x))
                break
            heapq.heappop(shortest[cur])
            
        cur = centroid[cur]
    return ret if ret != sys.maxsize else -1


for _ in range(N-1):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

dfs(1, 0) # initialize depth (after dp for LCA)
centroidDecomp(1, 0)

M = int(input())
for _ in range(M):
    q, param = map(int, input().split())
    if q == 1:
        update(param)
    else:
        print(query2(param))
