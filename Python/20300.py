import sys
input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split()))
T.sort()
ans = 0
if N%2:
    ans = T[-1]
    N -= 1

for i in range(N//2):
    ans = max(ans, T[i]+T[N-1-i])

print(ans)
