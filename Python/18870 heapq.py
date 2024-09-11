import sys
import heapq
N = int(sys.stdin.readline())
inp_line = list(map(int, sys.stdin.readline().split()))
ht = {}
heap = []
sorted_list = []

for x in inp_line:
    heapq.heappush(heap, x)
    # print(heap)

while heap:
    sorted_list.append(heapq.heappop(heap))

pre = '0'
idx = 0
for x in sorted_list:
    if x != pre:
        ht[x] = idx
        pre = x
        idx += 1

for x in inp_line:
    print(ht[x], end=' ')