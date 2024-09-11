import sys
import bisect
input = sys.stdin.readline

N, t = map(int, input().split())
pos = []
afterMove = []
i = 0

first, v = map(int, input().split())
afterMove.append(first+t*v)
# pos.append(x)
for _ in range(N-1):
    x, v = map(int, input().split())
    if x < first:
        i += 1
    afterMove.append(x+t*v)

afterMove.sort()
print(afterMove[i])
