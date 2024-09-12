# 트리이기 때문에 양방향 그래프이고 각 방향으로의 가중치가 같다
# 아무 노드를 루트로 두고 탐색해도 상관 없을듯
import sys
V = int(sys.stdin.readline())
visited = [False for x in range(V+1)]
# 인접 리스트 생성
adjacent_list = {x: [] for x in range(1, V+1)}  # src : [ (vertex, weight) ]
for _ in range(V):
    vertex, *adj, _ = map(int, sys.stdin.readline().split())
    dst = adj[::2]
    weight = adj[1::2]
    for i in range(len(dst)):
        adjacent_list[vertex].append((dst[i], weight[i]))

diameter = 0
# 루트를 1로 하고 dfs 를 돌려보자
#부분트리의 지름을 계산하고 확장시키는 식으로


# 종료지점이 리프 노드에 닿았을 때인데 간선의 길이로 할까? 아님 방문할 수 있는 노드가 없을 대로 할까?
def dfs(n):
    visited[n] = True

    # Base case (리프 노드일 경우)
    if len(adjacent_list[n]) == 1 and visited[adjacent_list[n][0][0]]:
        return 0

    # 리프 노드가 아닐 경우
    leaves = [0, 0]
    for nxt, w in adjacent_list[n]:
        if not visited[nxt]:
            leaf = dfs(nxt) + w
            if leaf > leaves[0]:
                leaves[1] = leaves[0]
                leaves[0] = leaf
            elif leaf > leaves[1]:
                leaves[1] = leaf

    global diameter
    diameter = max(diameter, leaves[0] + leaves[1])

    return leaves[0]


visited[1] = True
dfs(1)
print(diameter)
# 1. 부분트리에서의 지름을 구한다
# 2. 부분트리의 루트에서의 dfs는 높이를 반환
