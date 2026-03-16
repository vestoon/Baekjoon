import sys
sys.setrecursionlimit(91000)

"""
백트레킹+완탐 돌려 보면 저런 비스무리한 패턴이 나타남
결국 시간 안에 출력하려면 아래 방식으로 그냥 바로 출력 하는 게 정해인듯
"""
N = int(input())

ans = [
  ['N', 'A', 'Z'],
  ['A', 'Z', 'N'],
  ['Z', 'N', 'A']
]

# 그냥 ans 에 있는 거 N번씩 반복하기
for i in range(3):
  for _ in range(N):
    for j in range(3):
      print(ans[i][j]*N, end='')
    print()