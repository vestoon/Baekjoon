import sys
input = sys.stdin.readline

N = int(input())
total_cnt = 0
max_evo_cnt = 0
max_name = ""


for _ in range(N):
    name = input().rstrip()
    K, M = map(int, input().split())
    evo_cnt = 0

    while M >= K:
        evo_cnt += 1
        total_cnt += 1
        M -= K
        M += 2

    if evo_cnt > max_evo_cnt:
        max_evo_cnt = evo_cnt
        max_name = name

print(total_cnt)
print(max_name)