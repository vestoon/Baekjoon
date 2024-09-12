import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))


def check(n):  # 구간 점수의 최대값
    cnt = 1  # 구간의 수
    mini = arr[0]
    maxi = arr[0]

    for i in range(N):
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i])

        if maxi - mini > n:
            cnt += 1
            mini = arr[i]
            maxi = arr[i]

    return cnt <= M


hi = max(arr)-min(arr)
lo = -1
while lo + 1 < hi:
    mid = (lo + hi)//2
    if check(mid):
        hi = mid
    else:
        lo = mid
print(hi)