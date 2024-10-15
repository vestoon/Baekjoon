import sys
import heapq
input = sys.stdin.readline

"""
선후 관계가 정의된 여러 개의 힙이 있을 때 이를 정렬해서 출력해야 함
"""

N, M = map(int, input().split())
parent = [0 for x in range(N+1)] # parent가 0 이면 루트인 걸로
children = [[] for x in range(N+1)]
pq = []

for _ in range(M):
    A, B = map(int, input().split()) # A를 먼저 풀어야 한다. 
    parent[B] += 1
    children[A].append(B)

for i in range(1, N+1):
    if parent[i] == 0:
        heapq.heappush(pq, i)

while pq:
    cur = heapq.heappop(pq)
    print(cur, end=' ')
    for nxt in children[cur]:
        parent[nxt] -= 1
        if not parent[nxt]:
            heapq.heappush(pq, nxt)

