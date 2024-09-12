import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
adj_mat = [[0 for x in range(n)] for y in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if (not adj_mat[a][b]) or (adj_mat[a][b] and adj_mat[a][b] > c):
        adj_mat[a][b] = c

for k in range(n):
    for src in range(n):
        for dst in range(n):
            if not adj_mat[src][k] or not adj_mat[k][dst] or src == dst:
                continue
            if src == k or dst == k:
                continue
            via = adj_mat[src][k]+adj_mat[k][dst]
            adj_mat[src][dst] = min(adj_mat[src][dst], via) if adj_mat[src][dst] else via


for line in adj_mat:
    for x in line:
        print(x, end=' ')
    print()

