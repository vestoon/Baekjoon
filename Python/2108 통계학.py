import sys
N = int(sys.stdin.readline())
total = {}
M = -4001
m = 4001
s = 0

for g in range(N):
    n = int(sys.stdin.readline())
    total[n] = total.get(n, 0) + 1
    s +=n
    if n > M:
        M = n
    if n < m:
        m = n
totalsv = sorted(total.items(), key=lambda x: x[0])

print(int(round(s/N, 0)))  # 산술 평균

i = 1+N//2
for x in totalsv:
    i -= x[1]
    if i <= 0:
        print(x[0])
        break  # 중앙값

modes = []
f = 0
for x in totalsv:
    if x[1] > f:
        modes = [x[0]]
        f = x[1]
    elif x[1] == f:
        modes.append(x[0])
if len(modes) == 1:  # 최빈값
    print(modes[0])
else:
    print(modes[1])

print(M-m)  # 범위

