import sys
import heapq
input = sys.stdin.readline

# 그냥 N개 라인 들어올 때마다 길이 N을 유지하면서 힙으로 관리하면 되는거 아닌가?
N = int(input())
hq = []
for x in list(map(int, input().split())):
    heapq.heappush(hq, x)

for _ in range(N-1):
    for x in list(map(int, input().split())):
        if x <= hq[0]:
            continue

        heapq.heappop(hq)
        heapq.heappush(hq, x)

print(hq[0])
