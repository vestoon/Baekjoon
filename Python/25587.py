import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
parent = [x for x in range(N)]
size = [1 for x in range(N)]
water = [A[i]-B[i] for i in range(N)] # 노드 별 배수로의 총합
cnt = 0
for i in range(N):
    if water[i] < 0:
        cnt += 1

def union(x, y):
    global cnt
    x_parent = getParent(x)
    y_parent = getParent(y)
    if x_parent == y_parent: return
    if water[x_parent] < 0: # 원래 홍수가 날 도시들이었다면 일단 원상복구시킨다
        cnt -= size[x_parent]
    if water[y_parent] < 0:
        cnt -= size[y_parent]

    root = min(x_parent, y_parent)
    not_root = max(x_parent, y_parent)

    water[root] += water[not_root]
    size[root] += size[not_root]

    if water[root] < 0: # 합치고 나서도 홍수가 난다면 다시 더한다. 
        cnt += size[root]

    updateParent(x, root)
    updateParent(y, root)

def getParent(x):
    while parent[x] != x:
        x = parent[x]
    return x

# cur을 기준으로 위로 계속 올라가면서 parent를 전부  root로 바꿔 주는 함수
def updateParent(cur, root): 
    nxt = parent[cur]
    while nxt != cur:
        parent[cur] = root
        cur = nxt
        nxt = parent[cur]
    parent[cur] = root

"""
NM

각 노드가 각자의 parent와 size를 찾을 수 있어야 함
찾는 과정에서 parent가 수정되는건 필수인가? -> 사이즈에 문제가 생기지는 않는가?
그냥 루트 노드에만 올바른 값을 가지고 있는게 맞나?

연결 요소 별로 배수량의 총합과 크기를 관리해야 하는 문제
union find가 필요하려나?

union만 수행한다는 가정 하에 총합 N타임 이상 걸리지 않을지도 
"""

for _ in range(M):
    cmd, *args = map(int, input().split())

    if cmd == 1:
        x, y = args
        x -= 1
        y -= 1
        union(x, y)
    else:
        print(cnt)