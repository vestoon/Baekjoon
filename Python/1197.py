import sys
sys.setrecursionlimit(11000)
input = sys.stdin.readline

V, E = map(int, input().split())


def cycleCheck(a, b):
    ap = getParent(a)
    bp = getParent(b)
    if ap == bp:
        return True

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    if ap < bp:
        parent[bp] = ap
    else:
        parent[ap] = bp

    return False


def getParent(n):
    ret = parent[n]
    while parent[ret] != ret:
        ret = parent[ret]

    return ret

edges = []
parent = [x for x in range(V+1)]
cnt = 0  # Number of edges in spanning tree
ans = 0
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()

for c, a, b in edges:
    if cnt == V-1:
        break

    if not cycleCheck(a, b):
        cnt += 1
        ans += c

print(ans)


"""
5 7
1 2 2
1 3 3
2 3 1
2 4 3
2 5 2
3 5 1
4 5 5
"""
