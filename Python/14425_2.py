import sys
import bisect
input = sys.stdin.readline

N, M = map(int, input().split())
S = []
for _ in range(N):
  S.append(input().rstrip())
S.sort()

cnt = 0
for _ in range(M):
  word = input().rstrip()
  i = bisect.bisect_left(S, word)
  if 0<= i < len(S) and S[i] == word:
    cnt += 1

print(cnt)