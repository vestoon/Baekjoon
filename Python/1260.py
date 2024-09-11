nodeNumber, edgeNumber, start = map(int, input().split())
edges = {x: [] for x in range(1, nodeNumber+1)}
for i in range(edgeNumber):
    edge = tuple(map(int, input().split()))
    edges[edge[0]].append(edge[1])
    edges[edge[1]].append(edge[0])

for key in edges:  # 정렬
    edges[key].sort()


DFS = [start]
BFS = [start]

# DFS
while True:
    L = len(DFS)
    for i in range(L-1, -1, -1):  # DFS 리스트의 끝부터 탐색해서
        node = DFS[i]
        for nxt in edges[node]:  # 각 노드에서 갈 수 있는 노드 중에
            if nxt not in DFS:  # 아직 안가본 곳이 있으면
                DFS.append(nxt)
                break
        else:  # 이 원소에는 더 갈곳이 없다
            continue
        break  # 이렇게 하면
    else:
        break  # 아하 여기가 종료 조건인가?
for x in DFS:
    print(x, end=' ')
print()

# BFS
iB = 1
while iB != 0:
    iB = 0  # 탐색하는 층의 노드의 개수
    for node in BFS[-iB:]:  # n-1 층
        for nxt in edges[node]:  # n층
            if nxt not in BFS:
                BFS.append(nxt)
                iB += 1
for x in BFS:
    print(x, end=' ')


"""아니 이게 왜 5퍼에서 틀림?

6 5 6
5 4
4 6
2 3
3 13 1 2
1 2
1 6"""