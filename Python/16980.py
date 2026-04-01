import sys
input = sys.stdin.readline

"""
JO
I
형태 찾기

(i, j, k, l)
0 <= i < k < H
0 <= j < l < W
"""
H, W = map(int, input().split())

def sol(H: int, W: int) -> int:
  grid = [input().rstrip() for _ in range(H)]

  cnt_ingots = [[0 for x in range(W)] for y in range(H)] # (i, j) 포함 밑에 있는 ingot 수
  cnt_orbs = [[0 for x in range(W)] for y in range(H)] # (i, j) 포함 오른쪽에 있는 orb 수

  # cnt_orbs 초기화
  for i in range(H):
    cnt_orbs[i][-1] = 1 if grid[i][-1] == 'O' else 0
    for j in range(W-2, -1, -1):
      cnt_orbs[i][j] = cnt_orbs[i][j+1] + 1 if grid[i][j] == 'O' else cnt_orbs[i][j+1]

  # cnt_ingots 초기화
  for j in range(W):
    cnt_ingots[-1][j] = 1 if grid[-1][j] == 'I' else 0
    for i in range(H-2, -1, -1):
      cnt_ingots[i][j] = cnt_ingots[i+1][j] + 1 if grid[i][j] == 'I' else cnt_ingots[i+1][j]

  # 경우의 수 집계
  ret = 0
  for i in range(H):
    for j in range(W):
      if grid[i][j] != 'J': continue
      ret += cnt_ingots[i][j]*cnt_orbs[i][j]
  return ret

print(sol(H, W))