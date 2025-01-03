import sys
input = sys.stdin.readline
cnt = 0

N, M = map(int, input().split())
floor = [input().rstrip() for x in range(N)]

for i in range(N):
    for j in range(M):
        if floor[i][j] == '-':
            if j == 0:
                cnt += 1
            elif floor[i][j-1] != '-':
                cnt += 1
        else:
            if i == 0:
                cnt += 1
            elif floor[i-1][j] != '|':
                cnt += 1

print(cnt)