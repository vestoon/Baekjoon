import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
edge_list = []
adj_mat = [[0 for x in range(n)] for y in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if (not adj_mat[a][b]) or (adj_mat[a][b] and adj_mat[a][b] > c):
        adj_mat[a][b] = c

for v in range(n):
    for src in range(n):
        for dst in range(n):
            if src == dst:
                continue

            w = adj_mat[src][dst]
            if not w:
                continue

            for prev in range(n):
                if prev == dst:
                    continue

                if adj_mat[prev][src]:
                    adj_mat[prev][dst] = min(adj_mat[prev][src] + adj_mat[src][dst], adj_mat[prev][dst]) if adj_mat[prev][dst] else adj_mat[prev][src] + adj_mat[src][dst]

for line in adj_mat:
    for x in line:
        print(x, end=' ')
    print()



