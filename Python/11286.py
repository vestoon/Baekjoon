import sys
import heapq
input = sys.stdin.readline
abs_que = []

N = int(input())
for _ in range(N):
  x = int(input())
  if x:
    heapq.heappush(abs_que, (abs(x), x))
  else:
    print(heapq.heappop(abs_que)[1] if abs_que else 0)
    
