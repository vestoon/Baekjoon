import sys
# sys.setrecursionlimit(600000)
from collections import deque
input = sys.stdin.readline

N = int(input())
adj_list = [[] for x in range(N+1)]
depth = [-1 for x in range(N+1)]
parent = [-1 for x in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

q = deque()
q.append(1)
parent[1] = 0
depth[1] = 0
while q:
    cur = q.popleft()
    for nxt in adj_list[cur]:
        if depth[nxt] != -1:
            continue
        depth[nxt] = depth[cur] + 1
        parent[nxt] = cur
        q.append(nxt)

# print(depth)
# print(parent)

# def dfs_depth(cur: int, prev: int):
#     depth[cur] = depth[prev]+1

#     for nxt in adj_list[cur]:
#         if nxt == prev:
#             continue
#         parent[nxt] = cur
#         dfs_depth(nxt, cur)

# dfs_depth(1, 0)

def LCA(x:int, y:int)->int:
    parentX, parentY = x, y

    while depth[parentY] < depth[parentX]:
        parentX = parent[parentX]
    while depth[parentX] < depth[parentY]:
        # print('b1')
        parentY = parent[parentY]
    
    # print(parentX, parentY)
    while parentX != parentY:
        parentX = parent[parentX]
        parentY = parent[parentY]
    
    return parentX

# print(depth)
# print(parent)
M = int(input())
for _ in range(M):
    u, v = map(int, input().split())
    # print(u, v)
    print(LCA(u, v))