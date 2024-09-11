import sys
input = sys.stdin.readline

N, K = map(int, input().split())
exp = list(map(int, input().split()))
exp.sort()

ans = 0

for k in range(K):
    ans += exp[k]*k
for k in range(K, N):
    ans += exp[k]*K

print(ans)