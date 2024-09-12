import sys
import heapq
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

adj_list = {x: [] for x in range(1, n+1)}  # (weight, destination)
for _ in range(n-1):
    s, d, w = map(int, input().split())
    adj_list[s].append((w, d))

tree_diameter = 0


# 부분 트리의 높이를 반환, 동작하면서 트리 지름 최신화
def diameter_search(root):
    if not adj_list[root]:
        return 0

    global tree_diameter
    height = [0, 0]
    for w, sub in adj_list[root]:
        heapq.heappush(height, -1*(w+diameter_search(sub)))

    fst = -1*heapq.heappop(height)
    sec = -1*heapq.heappop(height)
    tree_diameter = max(tree_diameter, fst+sec)

    return fst


diameter_search(1)
print(tree_diameter)
