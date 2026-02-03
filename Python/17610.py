import sys
input = sys.stdin.readline

"""
추의 무게는 모두 다름,
주어진 추를 가지고 +-만 사용해서 만들 수 없는 경우의 수의 개수를 구해라.
"""
k = int(input())
G = list(map(int, input().split()))

S = sum(G) # < 2,600,000
canMake = [False for x in range(S + 1)]

cnt = 0 # 만들 수 있는 수의 개수
def search(acc, i):
  global cnt
  if i == k: return 

  for nxt in [acc, acc+G[i], acc-G[i]]:
    if 0 < nxt and not canMake[nxt]:
      canMake[nxt] = True
      cnt += 1

    search(nxt, i+1)

search(0, 0)
print(S - cnt)