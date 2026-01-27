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
discounts_info = [[] for _ in range(N)] # 물약 별 할인 정보

for n in range(N):
  p = int(input()) # n번째 물약에 대한 할인 정보의 수
  discount = []

  for _ in range(p):
    # 물약 a를 d만큼 할인해 준다.
    a, d = map(int, input().split()) # 인덱스 조정 필요
    discount.append((a-1 , d))

  discounts_info[n] = discount

min_cost = sum(C)
dp = [10001 for x in range((1 << N))] # 비트마스킹을 사용한 dp 

# 무지성 완탐하기
# itertools 사용, 비트마스킹 dp를 사용하여 같은 state에 대하여 백트레킹
for case in permutations([x for x in range(N)]):
  cur_discount = [0 for x in range(N)] # 현재 물약에 적용된 물약 정보
  cur_cost = 0
  cur_state = 0 # 현제 물약 구매 상태, 비트로 저장

  for portion in case:
    cur_cost += max(C[portion] - cur_discount[portion], 1)
    cur_state |= 1 << portion

    for a, d in discounts_info[portion]:
      # 현재 선택한 물품이 할인해 주는 목록들
      cur_discount[a] += d
    
    if dp[cur_state] < cur_cost:
      break
    dp[cur_state] = cur_cost
  else:
    # break가 안 걸린 경우 cur_cost <= min_ cost 이기 때문에 무조건 갱신
    min_cost = cur_cost

print(min_cost)

# PyPy3   : 1508ms , 114892KB
# Python3 : TLE (1%)
