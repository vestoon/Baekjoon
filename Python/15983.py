import sys
input = sys.stdin.readline
MOD = 1000000007
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

"""
T 범위가 작으니까 시작 좌표를 좌표를 조금 정규화해야 함
"""
# base를 기준으로 좌표 변환
def trans(x, y, base_x, base_y):
  return (x - base_x, y - base_y)

def sol():
  # -10,000 <= 좌표 <= 100,000
  s_x, s_y = map(int, input().split()) # 현재 위치
  T = int(input()) # 1 ~ 200
  b_x, b_y = s_x - T, s_y - T # base
  L = 2*T + 1 # 한 변의 길이

  # 목적지(집)
  h_x, h_y = map(int, input().split())
  h_x, h_y = trans(h_x, h_y, b_x, b_y)

  if not (0<=h_x<L and 0<=h_y<L):
    return 0

  # 건물
  buildings = [[False for x in range(L)] for y in range(L)] # 갈수 없는 곳
  N = int(input()) # 빌딩의 수: 0 ~ 100,000
  for _ in range(N):
    i_x, i_y = map(int, input().split())
    i_x, i_y = trans(i_x, i_y, b_x, b_y)
    if 0<= i_x<L and 0<= i_y<L:
      buildings[i_x][i_y] = True

  # 도착할 수 있는 경우의 수 계산
  dp = [[[0 for x in range(L)] for y in range(L)] for t in range(T+1)]

  ans = 0
  dp[0][T][T] = 1 # 시작 지점의 좌표
  for t in range(T):
    
    # 시간을 고려해서 탐색 범위를 좁힘
    for x in range(T-t, T+t+1):
      for y in range(T-t, T+t+1):
        if not dp[t][x][y]: continue

        for d in range(4):
          nx, ny = x+dx[d], y+dy[d]
          if not (0<=nx<L and 0<=ny<L): continue
          if buildings[nx][ny]: continue

          dp[t+1][nx][ny] = (dp[t+1][nx][ny] + dp[t][x][y])%MOD
    
    # 목적지에 도달한 경우 경우의 수 추가 후 삭제
    ans = (ans + dp[t+1][h_x][h_y])%MOD
    dp[t+1][h_x][h_y] = 0

  return ans

print(sol())