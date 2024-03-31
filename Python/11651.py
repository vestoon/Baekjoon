import sys
N = int(sys.stdin.readline())
co = []

for g in range(N):
    x, y = map(int, sys.stdin.readline().split())
    co.append((y, x))

for x in sorted(co):
    print(x[1], x[0])
