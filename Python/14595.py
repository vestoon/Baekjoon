import sys
input = sys.stdin.readline

"""
1 ~ N개의 방이 있는데 이중에서 (x, y)구간을 계속 합칠 때 방이 몇 개 남는지
아마도 union-find?

열고닫고만 기억하면 스택처럼 사용해서 공통 구간을 구할 수 있으려나?
"""

N = int(input()) # 2 ~ 1,000,000
M = int(input()) # 0 ~ 5,000

open = [0 for x in range(N+1)] # i번쨰 있는 열림 기호의 개수

for _ in range(M):
  # 1 <= x < y <= N
  x, y = map(int, input().split()) # 합치는 구간의 길이
  open[x] += 1
  open[y] -= 1

cnt = 0 # 구하려는 방의 수
acc = 0 # 아직 닫아야 하는 구간의 수
for i in range(1, N+1):
  if not acc: 
    cnt += 1
  acc += open[i]
print(cnt)