import sys
input = sys.stdin.readline

N, R = map(int, input().split())
rices = []
maxCnt = 0
maxI, maxJ = 0, 0


def check(i:int, j:int) -> int:
    cnt = 0
    for x, y in rices:
        if abs(x-i)**2 + abs(y-j)**2 <= R**2:
            cnt += 1

    return cnt


for _ in range(N):
    x, y = map(int, input().split())
    rices.append((x, y))


for i in range(-100, 101):
    for j in range(-100, 101):
        cnt = check(i, j)
        if cnt > maxCnt:
            maxCnt = cnt
            maxI, maxJ = i, j

# print(rices)
print(maxI, maxJ)
# print(maxCnt)