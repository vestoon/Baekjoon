import sys
input = sys.stdin.readline

N = int(input())

seq = list(map(int, input().split()))
comp = 1
ans = 0

for i in range(21):
    # print(comp)
    tmp = 0
    for n in seq:
        if n & comp:
            tmp += 1
    ans = max(ans, tmp)

    comp <<= 1

print(ans)