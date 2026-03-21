"""
안쪽에 박혀 있는 B는 사라지지 않는다. 
어차피 S로 바꾸고 뒤집기 때문에 뒤집은 후에 마지막이 B일 가능성은 없다. 

짝수는 소수가 아니기 때문에 앞부분 2,3 을 제외하면 소수를 만날 때마다 그냥 정직하게 S가 두 개씩 늘어나는 구조
"""

def sol2():
  N = int(input())
  if N == 2:
    print(0, 2)
    return
  if N == 1:
    print(1, 0)
    return
  
  isPrime = [True for x in range(N+1)]
  isPrime[0] = False
  isPrime[1] = False

  for x in range(2, N):
    if N < x*x: break
    if not isPrime[x]: continue
    
    cur = x*2
    while cur <= N:
      isPrime[cur] = False
      cur += x

  cntS = 0
  for i in range(1, N+1):
    if isPrime[i]:
      cntS += 1

  ans = cntS*2 - 1
  print(N-ans, ans)
  return

sol2()