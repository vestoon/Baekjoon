import sys
input = sys.stdin.readline
from collections import deque
"""
0-1 BFS 사용
직진하는 경우는 왼쪽에, 거울을 두는 경오는 오른 쪽에 추가
"""
house = []

# 시계 방향으로 각각 북, 동, 남, 서 방향
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 0: / 거울에 반사됐을 때 변하는 방향
# 1: \ 거울에 반사됐을 때 변하는 방향
reflect_d = [[1, 0, 3, 2],
            [3, 2, 1, 0]]

def sol():
  N = int(input()) # 집의 크기, 2 <= N < 50
  start = (-1, -1)
  end = (-1, -1)
  for i in range(N):
    """
    # : 문이 설치된 곳(항상 2개)
    ! : 거울을 설치할 수 있는 곳
    . : 빛이 통과할 수 있는 곳
    * : 벽이 있는 곳
    """
    line = list(input().rstrip())
    house.append(line)
    for j in range(N):
      if line[j] == '#':
        if start[0] == -1:
          start = (i, j)
        else:
          end = (i, j)
  
  return dfs(start, end, N)

def dfs(start: tuple[int], end: tuple[int], N: int) -> int:
  distance = [[[2501 for d in range(4)] for j in range(N)] for i in range(N)]
  dq = deque() # (i, j, distance)
  dq.append((start[0], start[1], 0)) # 여기서 3 번째 원소는 의미가 없다.
  distance[start[0]][start[1]][0] = 0

  while dq:
    ci, cj, cd = dq.popleft()

    if ci == end[0] and cj == end[1]:
      return distance[ci][cj][cd]
    
    if house[ci][cj] == '*': continue

    # 출발점일 경우에만 실행
    if house[ci][cj] == '#':
      for nd in range(4):
        ni, nj = ci + direction[nd][0], cj + direction[nd][1]
        if 0 <= ni < N and 0 <= nj < N and distance[ci][cj][cd] < distance[ni][nj][nd]:
          distance[ni][nj][nd] = distance[ci][cj][cd]
          dq.append((ni, nj, nd))
      continue

    # house[ci][cj]가 . 또는 ! 일 때만 실행
    # 거울을 설치하지 않고 직진하는 경우
    ni, nj = ci + direction[cd][0], cj + direction[cd][1]
    if 0 <= ni < N and 0 <= nj < N and distance[ci][cj][cd] < distance[ni][nj][cd]:
      distance[ni][nj][cd] = distance[ci][cj][cd]
      dq.appendleft((ni, nj, cd))
    
    if house[ci][cj] == '!':
      # / 거울을 설치하는 경우
      nd = reflect_d[0][cd]
      ni, nj = ci + direction[nd][0] , cj + direction[nd][1]
      if 0 <= ni < N and 0 <= nj < N and distance[ci][cj][cd] + 1 < distance[ni][nj][nd]:
        distance[ni][nj][nd] = distance[ci][cj][cd] + 1
        dq.append((ni, nj, nd))
      
      # \ 거울을 설치하는 경우
      nd = reflect_d[1][cd]
      ni, nj = ci + direction[nd][0] , cj + direction[nd][1]
      if 0 <= ni < N and 0 <= nj < N and distance[ci][cj][cd] + 1 < distance[ni][nj][nd]:
        distance[ni][nj][nd] = distance[ci][cj][cd] + 1
        dq.append((ni, nj, nd))
  
print(sol())

