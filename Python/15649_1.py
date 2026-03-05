N, M = map(int, input().split())

used = [False for x in range(N)]

def permutation(acc):
  if len(acc) == M:
    print(*acc)
  
  for nxt in range(N):
    if not used[nxt]:
      used[nxt] = True
      permutation(acc+[nxt+1])
      used[nxt] = False

permutation([])