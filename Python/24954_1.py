import sys
from itertools import permutations
input = sys.stdin.readline

"""
물약은 한 번씩만 구매할 수 있음
백트레킹을 적용시킨 완전 탐색 문제

1. 순열을 기준으로 완전 탐색
물약의 구매 상태를 비트로 저장(비트마스킹)하면 중간 과정에 대해서 백트레킹이 가능
재귀를 사용하면 할인 정보를 메모리를 아끼며 계산 가능

2. 비트마스킹을 백트레킹이 아니라 dp로 사용
0 < i < 2**N 순서로 dp 값을 계산한다면 각각의 i에 대해서 dp[i]를 계산하기 위해 필요한 다른 dp값들이
이미 계산되어 있다는 것이 보장되기 때문

다만 할인 정보 또한 따로 저장해야 한다.
"""

N = int(input())
C = list(map(int, input().split())) # 물약의 시작 가격
discounts = [[] for _ in range(N)] # 물약 별 할인 정보

for n in range(N):
  p = int(input()) # n번째 물약에 대한 할인 정보의 수
  discount = []

  for _ in range(p):
    # 물약 a를 d만큼 할인해 준다.
    a, d = map(int, input().split()) # 인덱스 조정 필요
    discount.append((a-1 , d))
  discounts[n] = discount

cost = sum(C)

# 무지성 완탐하기
# itertools 사용, 백트렉킹 없음
for case in permutations([x for x in range(N)]):
  # 일단 복사
  cur_cost = 0
  cur_discount = [0 for x in range(N)]

  for cur in case:
    # 구매
    cur_cost += max(C[cur] - cur_discount[cur], 1)

    # 할인 적용
    for a, d in discounts[cur]:
      cur_discount[a] += d

  # 갱신
  cost = min(cost, cur_cost)

print(cost)

# PyPy3   : 1960ms , 111412 KB
# Python3 : TLE (1%)