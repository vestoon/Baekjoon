import sys
input = sys.stdin.readline

"""
김밥의 수: 1 <= N <= 1,000,000
꼬다리의 길이: 1 <= K <= 1,000,000,000
김밥 조각의 최소 개수: 1 <= M <= 1,000,000,000
"""
gimbobs = []

def sol():
  N, K, M = map(int,input().split())

  for _ in range(N):
    L = int(input())
    if 2*K <= L:
      gimbobs.append(L- 2*K)
    elif K < L:
      gimbobs.append(L - K)

  if not gimbobs: return -1
  lo, hi = 1, max(gimbobs) + 1
  if check(lo) < M:
    return -1
  
  while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid) < M:
      hi = mid
    else:
      lo = mid
  return lo

# P = x일 때 만들 수 있는 김밥의 수
def check(x):
  ret = 0
  for gimbob in gimbobs:
    ret += gimbob//x
  return ret

print(sol())