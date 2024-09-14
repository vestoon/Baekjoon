import sys
input = sys.stdin.readline

N = int(input())

idx = [0 for x in range(N+1)]

for i in range(N):
    idx[int(input())] = i

cnt = 0
for i in range(1, N):
    if idx[i] > idx[i+1]:
        cnt += 1

# print(idx)
print(cnt)