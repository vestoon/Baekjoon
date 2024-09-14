import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
parent = list(map(int, input().split()))
parent_cent = [0 for x in range(N+1)]
dist = [sys.maxsize for x in range(N+1)]

# 재귀를 사용해서 centroid decompostion을 해보자
def centroidDecomp(l:int, r:int, prev: int):
    # print(l, r, prev)
    if l == r:
        parent_cent[r] = prev
        return
    if l+1 == r:
        parent_cent[l] = prev
        parent_cent[r] = l
        return
    
    # 1 2 3 4 5 6 7?
    mid = (l+r)//2
    parent_cent[mid] = prev
    centroidDecomp(l,mid-1, mid) # 자기 자신이 또 centroid에 포함될 수 있으니까 mid는 범위에서 제외하자
    centroidDecomp(mid+1, r, mid)


def update(v:int):
    dist[v] = 0
    p = parent_cent[v]
    while p:
        dist[p] = min(dist[p], abs(v-p))
        p = parent_cent[p]


def find(v:int) -> int:
    ret = dist[v]
    p = parent_cent[v]

    while p:
        ret = min(ret, abs(v-p)+dist[p])
        p = parent_cent[p]
    
    return ret if ret != sys.maxsize else -1


centroidDecomp(1, N, 0)
# print(parent_cent)
for _ in range(Q):
    c, v = map(int, input().split())
    if c == 1:
        update(v)
    else:
        print(find(v))