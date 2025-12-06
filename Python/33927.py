import sys
input = sys.stdin.readline

N = int(input())
chess_board = [list(map(int, input().split())) for x in range(N)]
visited = [[False for x in range(N)] for y in range(N)]

dx = (1, 1, -1, -1, 2, 2, -2, -2)
dy = (2, -2, 2, -2, 1, -1, 1, -1)


def search(i: int, j: int, acc: int):
  idx = i*N + j
  if idx == N*N:
    return acc
  
  ni, nj = (idx+1)//N, (idx+1)%N
  ret = search(ni, nj, acc)
  
  if check(i, j):
    visited[i][j] = True
    ret = max(ret, search(ni, nj, acc+chess_board[i][j]))
    visited[i][j] = False

  return ret

# 현재 위치에 나이트를 둘 수 있는지 확인
def check(i: int, j: int):
  for d in range(8):
    si, sj = i+dx[d], j+dy[d]
    if not (0 <= si < N and 0 <= sj < N):
      continue
    if visited[si][sj]:
      return False
  
  return True

print(search(0, 0, 0))
