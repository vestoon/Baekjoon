# 자식 노드에서 목적지까지 가는 경로가 없을 수도 있나?
# 모든 학생들이 집에서 목적지까지 갈 수는 있게 주어진다고 했기 때문에 하위 트리에서 목적지를 못 찾을 걱정은 없다
# 각 노드를 클래스처럼 만들어서 이미 최단거리를 계산한 경우는 제외해야 하나?
import sys
# N: 마을의 개수, M: 간선의 개수, X: 파티 장소
N, M, X = map(int, sys.stdin.readline().split())
INF = int(1e9)

# 방문 리스트
visited = [False for _ in range(N+1)]
# 인접 행렬 생성
adjacent_list = [[] for x in range(N+1)]  # (nxt, weight)
shortest_path = [False for x in range(N+1)]  # 각 vertex 에서 X 까지 갈 수있는 최단 거리를 찾으면 저장
for _ in range(M):
    src, dst, weight = map(int, sys.stdin.readline().split())
    adjacent_list[src].append((dst, weight))


def dfs(src, dst):
    if src == dst:
        return 0

    sp = shortest_path[src]
    if dst == X and sp:
        return sp
    # print('src', src, 'dst', dst)

    visited[src] = True
    m = INF
    # is_path = False  # 더 이상 탐색할 길이 없으면 False

    for nxt, w in adjacent_list[src]:
        # print('nxt', nxt)
        if visited[nxt]:  # 방문했거나 길이 없으면 패스
            continue

        d = dfs(nxt, dst)
        if d is not None:
            m = min(m, d+w)

    visited[src] = False
    if m:
        return m


M = 0
for vertex in range(1, N+1):
    # print('v', vertex)
    if vertex == X:
        continue
    # print(visited)
    shortest_path[vertex] = dfs(vertex, X)
    # print(shortest_path[vertex])
    # print(visited)
    M = max(M, shortest_path[vertex] + dfs(X, vertex))

print(M)
