import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(0)

i = 0
j = X-1
M = 0
cur = sum(arr[:X])
cnt = 0

while j != N:
    if cur == M:
        cnt += 1
    elif M < cur:
        M = cur
        cnt = 1

    cur -= arr[i]
    i += 1
    j += 1
    cur += arr[j]

if M:
    print(M)
    print(cnt)
else:
    print('SAD')