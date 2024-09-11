import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
Tree = {x: [] for x in range(1, N+1)}  # 정수: 리스트
visited = [0 for x in range(N+1)]
count = 0
for g in range(M):
    edge = tuple(map(int, sys.stdin.readline().split()))
    Tree[edge[0]].append(edge[1])
    Tree[edge[1]].append(edge[0])


bfs = [1]
visited[1] = 1
while bfs:
    count += 1
    # print(bfs[0])
    for x in Tree[bfs[0]]:
        if not visited[x]:
            bfs.append(x)
            visited[x] = 1
    bfs.remove(bfs[0])

print(count-1)

