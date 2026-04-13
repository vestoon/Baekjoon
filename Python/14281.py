def check_convex(A:list[int]) -> bool:
  for i in range(1, len(A)-1):
    if A[i-1] + A[i+1] < 2*A[i]:
      return False
    
  return True

def solve():
  N = int(input())
  A = list(map(int, input().split()))
  ret = 0

  while not check_convex(A):
    for i in range(1, N-1):
      if A[i-1] + A[i+1] < 2*A[i]:
        target = (A[i-1]+A[i+1])//2
        ret += A[i] - target
        A[i] = target
  
  return ret

print(solve())