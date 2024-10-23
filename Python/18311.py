import sys
input = sys.stdin.readline

N, K = map(int, input().split())
course = list(map(int, input().split()))
cur = 0

for i in range(N):
    if K < 0:
        break
    cur  = i
    K -= course[i]
    
for i in range(N-1, -1, -1):
    if K < 0:
        break
    cur  = i
    K -= course[i]



print(cur+1)