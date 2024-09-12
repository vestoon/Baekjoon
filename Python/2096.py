import sys
input = sys.stdin.readline

N = int(input())

dp_min = [0, 0, 0]
dp_max = [0, 0, 0]

for _ in range(N):
    line = list(map(int, input().split()))

    tmp_min = [min(dp_min[0], dp_min[1]), min(dp_min), min(dp_min[1], dp_min[2])]
    tmp_max = [max(dp_max[0], dp_max[1]), max(dp_max), max(dp_max[1], dp_max[2])]

    for j in range(3):
        tmp_min[j] += line[j]
        tmp_max[j] += line[j]

    dp_min = tmp_min
    dp_max = tmp_max

print(max(dp_max), min(dp_min))
