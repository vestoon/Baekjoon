import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
arr = list(map(int ,input().split()))
X = int(input())

info = defaultdict(int)
cnt = 0

for x in arr:
    cnt += info[X-x]
    info[x] += 1

print(cnt)