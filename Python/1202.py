import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = []
bags = []
slot = [False for x in range(K)]
ans = 0
for _ in range(N):
    M, V = map(int, input().split())  # M: magnitude, V: value
    heapq.heappush(jewels, (M, V))
for _ in range(K):
    C = int(input())
    bags.append(C)
bags.sort()

jewelValue = []  # Maxheap of value of available jewel
for bag in bags:

    while jewels and jewels[0][0] <= bag:
        heapq.heappush(jewelValue, -heapq.heappop(jewels)[1])

    if jewelValue:
        ans -= heapq.heappop(jewelValue)

print(ans)

"""
4 4
2 1
2 2
2 3
2 4
1
1
2
2
"""
"7"
