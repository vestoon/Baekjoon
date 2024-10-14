import sys
input = sys.stdin.readline

"""
대놓고 MST 구하기

프림: O(E + VlogV) 꼭 피보나치 힙이 필요한가?
크루스칼: O(ElogV)
일단 크루스칼을 이용해 풀어보자
"""

# N: 집의 개수, M: 길의 개수
N, M = map(int, input().split())
parent = [x for x in range(N+1)]
edges = []
ans = 0
last = 0


def getParent(x:int) ->int:
    if parent[x] == x:
        return x
    
    parent[x] = getParent(parent[x])
    return parent[x]

def union(x:int, y:int):
    xp, yp = getParent(x), getParent(y)

    if xp < yp:
        parent[yp] = xp
    else:
        parent[xp]  = yp


for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))
edges.sort()

for c, a, b in edges:
    if getParent(a) == getParent(b): continue

    last = c
    ans += c
    union(a, b)

print(ans - last)