import sys
from collections import defaultdict
input = sys.stdin.readline

# N: 상자의 개수
# K: 규칙의 개수
# D: 도토리의 개수
N, K, D = map(int, input().split())
rules = []

for _ in range(K):
  A, B, C = map(int, input().split())
  rules.append((A, B, C))

# 해당 위치까지 박스를 열었을 때 얻을 수 있는 도토리의 수
def check(i):
  ret = 0
  for a, b, c in rules:
    if i < a: continue # 얻을 수 있는 도토리가 없는 규칙

    # a <= i
    ret += 1 + (min(i, b)-a)//c
  return ret

lo, hi = 1, N
while lo + 1 < hi:
  mid = (lo+hi)//2

  if check(mid) < D:
    lo = mid
  else:
    hi = mid

print(hi)