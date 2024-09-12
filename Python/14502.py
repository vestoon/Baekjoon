import sys
import collections
input = sys.stdin.readline

dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)


def spread(y, x, m):
    q = collections.deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for n in range(4):
            nx, ny = x + dx[n], y + dy[n]
            if 0 <= nx < M and 0 <= ny < N and m[ny][nx] == 0:
                m[ny][nx] = 2
                q.append((ny, nx))


def cnt_saftey_area(m):
    cnt = 0
    for x in m:
        for y in x:
            if y == 0:
                cnt += 1
    return cnt


N, M = map(int, input().split())
virus = []
blank = []

mp = []
for i in range(N):
    tmp = list(map(int, input().split()))
    # print(tmp)
    for j in range(M):
        if tmp[j] == 2:
            virus.append((i, j))
        elif tmp[j] == 0:
            blank.append((i, j))

    mp.append(tmp)

ret = 0

for i in range(len(blank)):
    for j in range(i+1, len(blank)):
        for k in range(j+1, len(blank)):
            mpcopy = [x[:] for x in mp]
            b1, b2, b3 = blank[i], blank[j], blank[k]
            for cor in [b1, b2, b3]:
                mpcopy[cor[0]][cor[1]] = 1

            for v in virus:
                spread(v[0], v[1], mpcopy)
            ret = max(ret, cnt_saftey_area(mpcopy))

print(ret)
