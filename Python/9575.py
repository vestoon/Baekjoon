import sys
input = sys.stdin.readline

def sol() -> int:
  ret = 0
  can_make = [False for x in range(100000)]
  input()
  A = list(map(int, input().split()))
  input()
  B = list(map(int, input().split()))

  input()
  C = list(map(int, input().split()))

  for a in A:
    for b in B:
      for c in C:
        cur = a + b + c
        if can_make[cur]: continue

        for s in str(cur):
          if s != '5' and s != '8':
            break
        else:
          can_make[cur] = True
          ret += 1
  return ret

T = int(input())
for tc in range(T):
  print(sol())
