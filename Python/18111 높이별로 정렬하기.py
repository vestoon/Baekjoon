import sys
N, M, B = map(int, sys.stdin.readline().split())  # 세로, 가로, 개수

land ={}

for r in range(N):
    for co in map(int, sys.stdin.readline().split()):
        land[co] = land.get(co, 0) + 1
# print('land =', land)
timecost = 128000000
high = 0

for z in range(257):
    lower = 0
    higher = 0
    for h in land:
        if h > z:
            higher += (h - z)*land[h]
        else:
            lower += (z - h)*land[h]

    if B+higher < lower:
        continue
    t = 2*higher + lower
    if t <= timecost:
        timecost = t
        high = z

print(timecost, high)


