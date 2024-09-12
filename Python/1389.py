N, M = map(int, input().split())  # N: 유저의 수, M: 친구 관계의 수
edges = {n: [] for n in range(1, N+1)}
for m in range(M):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)


preBacon = 500000  # 절대 넘을 수 없는 베이컨 수
ans = 0  # output
for person in range(1, N+1):  # person 은 사람번호
    bacon = 0  # 케빈 베이컨의 수
    BFS = [person]  # 탐색 시작
    layerSize = 1  # 탐색하는 층의 노드의 개수
    layerDepth = 1  # 사람 사이의 거리
    while layerSize != 0:
        layerSize = 0  # layerSize 초기화
        for node in BFS[-layerSize:]:
            for nxt in edges[node]:
                if nxt not in BFS:
                    layerSize += 1
                    bacon += layerDepth
                    BFS.append(nxt)
        layerDepth += 1

    if bacon < preBacon:  # 이전 값보다 작은지 계산
        ans = person
        preBacon = bacon

# print(BFS)
print(ans)




