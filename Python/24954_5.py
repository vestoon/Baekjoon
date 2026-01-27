import sys
from collections import deque
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

dp = [10001 for x in range((1 << N))] # 비트마스킹을 사용한 dp 

# deque, dfs로 permutation 구현
# state별로 dp 사용
# rest 상태만 보고 state를 판단할 수 있으면 좋을 텐데 그게 안돼서 좀 아쉬움
def dfs_permutation(acc, state, cur_discount, C, rest):
  if not rest: # state가 11...인 상태
    dp[state] = min(dp[state], acc)
    return

  if dp[state] <= acc: return
  dp[state] = acc

  l = len(rest) # rest 길이 만큼 반복
  for _ in range(l):
    nxt = rest.popleft()

    # 물약 구매
    state |= 1 << nxt # state에 추가
    for a, d in discounts_info[nxt]:
      cur_discount[a] += d
    
    cost = max(C[nxt] - cur_discount[nxt], 1) # 다음 물약을 구매하는데 드는 비용
    dfs_permutation(acc + cost, state, cur_discount, C, rest) # rest를 하나 줄인 상태로 재귀 호출

    # 원상 복구
    state ^= 1 << nxt
    for a, d in discounts_info[nxt]:
      cur_discount[a] -= d
    
    rest.append(nxt) # 사용한 원소를 큐 반대편에 다시 삽입
    
dfs_permutation(0, 0, [0 for x in range(N)], C, deque([x for x in range(N)]))
print(dp[-1])

# PyPy3   : 132ms , 115032KB
# Python3 : 80ms  , 34992KB