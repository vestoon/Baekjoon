import itertools

N, M = map(int, input().split())

for comb in itertools.permutations([x for x in range(1, N+1)], M):
  print(*comb)