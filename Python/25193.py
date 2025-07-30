import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

cnt = 0
for s in S:
    if s == 'C':
        cnt += 1
rest = N-cnt

print(cnt//(rest+1) + 1 if cnt%(rest+1) else cnt//(rest+1))