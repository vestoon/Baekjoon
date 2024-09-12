# Second version using Floyd-Warshall
# less memory but more time
import sys
input = sys.stdin.readline
INF = 1501

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
adj_list = [[INF for x in range(n+1)] for y in range(n+1)]
edge_list = []

for _ in range(r):
    a, b, l = map(int, input().split())
    adj_list[a][b] = l
    adj_list[b][a] = l
    edge_list.append((a, b, l))

for d in range(n+1):
    adj_list[d][d] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist = adj_list[i][k] + adj_list[k][j]
            if dist <= m and dist < adj_list[i][j]:
                adj_list[i][j] = dist

ans = 0
for src in range(1, n+1):
    item = 0
    for v in range(1, n+1):
        if adj_list[src][v] <= m:
            item += items[v]

    ans = max(ans, item)

print(ans)
"""
4 5 4
1 2 3 4 
1 2 5
1 3 1
2 3 2
2 4 1
"""