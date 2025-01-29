import sys
from collections import defaultdict
input = sys.stdin.readline

Q = int(input())
height = defaultdict(int)

for _ in range(Q):
    cmd, i = map(int, input().split())

    if cmd == 1:
        h = 0
        for x in range(i, i+4):
            h = max(h, height[x])
        for x in range(i, i+4):
            height[x] = h+1
    elif cmd == 2:
        height[i] += 4
    else: # cmd == 3
        print(height[i])

