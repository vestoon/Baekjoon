import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
v0, p0, s0 = map(int, input().split())
state0 = v0+p0+s0
member = []

# for i in range(1, N+1):
#     v, p, s = map(int, input().split())
#     state = v+p+s
#     if state <= state0:
#         heapq.heappush(member, (-state, i))

# print(0, end=' ')
# for _ in range(M-1):
#     if not member:
#         break
#     cur = heapq.heappop(member)
#     print(cur[1], end=' ')

for i in range(1, N+1):
    v, p, s = map(int, input().split())
    state = v+p+s
    if state <= state0:
        member.append((state, i))

member.sort(reverse=True)
print(0, end=' ')
for i in range(min(M-1, len(member))):
    print(member[i][1], end=' ')

