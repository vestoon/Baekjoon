import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
comb = defaultdict(int)
cnt = 0

for i in range(n):
    tmp = 0
    for j in range(i, n):
        tmp += A[j]
        comb[tmp] += 1

for i in range(m):
    tmp = 0
    for j in range(i, m):
        tmp += B[j]
        cnt += comb[T-tmp]

# hash를 통해 구현
# print(comb)
print(cnt)