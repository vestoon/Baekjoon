import sys
input = sys.stdin.readline

"""
시뮬레이션 문제 같은데
일단 최대한 많은 사람이 우산 전부 써서 넘어가고
돌아올 때는 한 명만 모든 우산을 다 가져온다.
"""

T = int(input()) # 1 ~ 1000

for tc in range(T):
  """
  N: 사람 수
  M: 우산 수
  K: 우산 하나에 넣을 수 있는 사람 수
  """
  N, M, K = map(int, input().split()) # 1 ~ 10
  # 우산에 한 명밖에 못 들어가고 1개밖에 없고 사람 수보다 적어야 함
  if K == 1 and M == 1 and M < N:
    print(-1)
    continue

  cnt = 0 # 이동 횃수

  while 0 < N:
    cnt += 1
    N -= K*M
    if 0 < N:
      cnt += 1
      N += 1
  print(cnt)