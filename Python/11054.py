import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

inc = [0 for _ in range(N)]
dec = [0 for _ in range(N)]

# increasing sequence
inc[0] = 1
for i in range(1, N):
    tmp = 1
    for prev in range(i):
        if seq[i] > seq[prev]:
            tmp = max(tmp, inc[prev]+1)

    inc[i] = tmp

# decreasing sequence
dec[-1] = 1
for i in range(N-2, -1, -1):
    tmp = 1
    for prev in range(N-1, i, -1):
        if seq[i] > seq[prev]:
            tmp = max(tmp, dec[prev]+1)

    dec[i] = tmp

ans = 0
for i in range(N):
    ans = max(ans, inc[i]+dec[i]-1)

print(ans)