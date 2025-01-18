import sys
input = sys.stdin.readline

N = int(input())
info = []
for _ in range(N):
    inp = input().split()
    name= inp[0]
    korean, math, english = map(int, inp[1:])

    info.append((name, korean, math, english))

info.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))

for x in info:
    print(x[0])