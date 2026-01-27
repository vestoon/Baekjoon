import sys
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

# 비트마스킹을 사용한 dp
dp_cost = [10001 for x in range((1 << N))] # state에 비용 정보, 갱신 가능
dp_discount = [[] for x in range(1 << N)]  # state에 따른 할인 정보, 저장용, 갱신 x

# 1 ~ 2**N까지 button-up dp
# 
dp_cost[0] = 0 # 초기값 설정
for cur_state in range(1, 1 << N):
  cur_cost = 10001 # 현재 상태의 최소 비용

  for prev in range(N):
    if not (cur_state & (1 << prev)): continue
    prev_state = cur_state ^ (1 << prev) # prev를 사기 이전 상태

    # 이전 상태에 대한 할인 정보가 저장돼있지 않은 경우
    if not dp_discount[prev_state]:
      prev_discount = [0 for x in range(N)]
      for p in range(N):
        if prev_state & (1 << p):
          for a, d in discounts_info[p]:
            prev_discount[a] += d
      # 저장
      dp_discount[prev_state] = prev_discount

    prev_cost = dp_cost[prev_state] + max(C[prev] - dp_discount[prev_state][prev], 1)
    cur_cost = min(cur_cost, prev_cost)
  
  dp_cost[cur_state] = cur_cost

print(dp_cost[-1])

# PyPy3   : 120ms , 1109766KB
# Python3 : 44ms  , 33432KB