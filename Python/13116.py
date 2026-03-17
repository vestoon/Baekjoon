import sys
input = sys.stdin.readline

def sol(A: int, B: int) -> int:
  M = max(A, B)
  visited = [False for x in range(M+1)] # A가 위로 올라가는 경로

  while A != 1:
    visited[A] = True
    A //= 2
  
  while B != 1:
    if visited[B]:
      return B
    B //= 2

  # 혹시 B가 시작부터 1인 경우, 일단 1은 무조건 옳음
  return 1

T = int(input())
for tc in range(T):
  A, B = map(int, input().split())
  print(sol(A, B)*10)
  
