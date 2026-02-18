import sys
input = sys.stdin.readline

"""
정렬 후 이분탐색 하면 됨
"""

N, M = map(int, input().split())
S = []
for _ in range(N):
  word = input().rstrip()
  S.append(word)
S.sort()

def check(i, word):
  if i == -1: return False
  if i == N: return True
  return word <= S[i]

cnt = 0
for _ in range(M):
  word = input().rstrip()

  lo, hi = -1, N
  while lo+1 < hi:
    mid = (lo+hi)//2

    if check(mid, word):
      hi = mid
    else:
      lo = mid
  
  if 0 <= hi < N and S[hi].startswith(word):
    cnt += 1

print(cnt)