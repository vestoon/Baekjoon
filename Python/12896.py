import sys
input = sys.stdin.readline
sys.setrecursionlimit(110000)

"""
그냥 트리 지름구하는 로직 구한 뒤에 반으로 나눔
트리의 가중치가 없기 때문에 반으로 나눠서 답을 찾을 수 있다.
"""
INF = float("inf")
N = int(input()) # 2 ~ 100,000
adj_list = [[] for x in range(N+1)]

for _ in range(N-1):
  u, v = map(int, input().split())
  adj_list[u].append(v)
  adj_list[v].append(u)

diameter = 0 # 트리의 지름

# 지름 계산, 트리의 높이 반환
def cal_diameter(cur:int, prev: int):
  global diameter
  radiuses = [0, 0] # 하위 트리의 높이들 저장, 개수가 부족할 때를 대비해 0을 채움

  for nxt in adj_list[cur]:
    if nxt == prev: continue

    radiuses.append(cal_diameter(nxt, cur)+1)
  
  radiuses.sort()
  diameter = max(diameter, sum(radiuses[-2:])) # cur이 트리의 지름에 속한다면 여기서 갱신
  return radiuses[-1]

cal_diameter(1, 0)
print(diameter//2 +1 if diameter%2 else diameter//2)