import sys
N, M = map(int, input().split())


pb =[0] + list(map(int, input().split()))
for i in range(1, N+1):
    pb[i] += pb[i-1]


for x in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(pb[j] - pb[i-1])