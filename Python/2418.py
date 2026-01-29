import sys
input = sys.stdin.readline

dy = (1, 1, 0, -1, -1, -1, 0, 1)
dx = (0, 1, 1, 1, 0, -1, -1, -1)
W, H, L = map(int, input().split())
grid = []

for _ in range(W):
  grid.append(input().rstrip())

target = input().rstrip()
cnt = 0

# dp[i][j][k] : (i,j) 위치에서 target의 k 번째를 완성했을 때 target을 만들 수 있는 경우의 수
dp =[[[0 for k in range(L)] for j in range(H)] for i in range(W)]

# k=0 초기값 설정
for i in range(W):
  for j in range(H):
    if grid[i][j] == target[0]:
      dp[i][j][0] += 1

for k in range(1, L):
  for i in range(W):
    for j in range(H):
      for d in range(8):
        ni, nj = i+dx[d], j+dy[d]
        if not (0<=ni<W and 0<=nj<H): continue
        if grid[i][j] != target[k]: continue

        dp[i][j][k] += dp[ni][nj][k-1]

ans = 0
for i in range(W):
  for j in range(H):
    ans += dp[i][j][-1]

print(ans)