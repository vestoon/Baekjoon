import sys
import heapq
input = sys.stdin.readline

"""
아 작아 지는 건 괜찮은데 커지는 건 다음 값을 추적하지 못하는 구나
그냥 힙 만들어서 닥치는 대로 넣은 다음에 뽑을 때 일치하지 않으면 버리는 걸로?
어차피 불일치하는 쓰레기 값은 넣은 횃수만큼만 나오고 다시 나오지 않기 때문에 최대 100,000번 발생
"""

N, M = map(int, input().split())
route_a = list(map(int, input().split()))
route_b = list(map(int, input().split()))

# (값, 인덱스)로 힙 만들기
heap_a = [(route_a[i], i) for i in range(N)]
heap_b = [(route_b[i], i) for i in range(M)]
heapq.heapify(heap_a)
heapq.heapify(heap_b)

# 힙큐에서 최소값 뽑기, 일치하지 않는 거 나오면 버리기
def get_min(heap, route):
  cur_val, cur_i = heap[0]

  while route[cur_i] != cur_val:
    heapq.heappop(heap)
    cur_val, cur_i = heap[0]
  
  return cur_i

K = int(input())
for _ in range(K):
  inp = input().rstrip()
  if inp[0] == 'L':
    # 현재 최소값 출력
    print(get_min(heap_a, route_a) + 1, get_min(heap_b, route_b) + N + 1)
  else: # inp[0] == 'U'
    # x번 길의 인구를 y로 바꾸기
    x, y = map(int, inp[2:].split())
    x -= 1
    if x < N:
      heapq.heappush(heap_a, (y, x))
      route_a[x] = y
    else:
      x -= N
      heapq.heappush(heap_b, (y, x))
      route_b[x] = y


