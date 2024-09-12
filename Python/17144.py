import sys
input = sys.stdin.readline

dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)

R, C , T = map(int, input().split())
house = [list((map(int, input().split())))for x in range(R)]
nxt = [[0 for x in range(C)] for y in range(R)]

vac = []

for i in range(R):
    for j in range(C):
        if house[i][j] == -1:
            vac.append((i, j))

up, down = vac


def spread():
    nxt[up[0]][up[1]] = -1
    nxt[down[0]][down[1]] = -1
    for i in range(R):
        for j in range(C):
            if house[i][j] <= 0:
                continue
            # print('ij', i, j)  #
            sub = house[i][j]//5
            for n in range(4):
                ni, nj = i+dy[n], j + dx[n]
                # print(ni, nj)
                if 0 <= ni < R and 0 <= nj < C and (ni, nj) != up and (ni, nj) != down:
                    nxt[ni][nj] += sub
                    house[i][j] -= sub
            nxt[i][j] += house[i][j]


def circul():
    # upper circle
    for i in range(up[0]-1, 0, -1):
        house[i][0] = house[i-1][0]
    for j in range(C-1):
        house[0][j] = house[0][j+1]
    for i in range(up[0]):
        house[i][C-1] = house[i+1][C-1]
    for j in range(C-1, 0, -1):
        house[up[0]][j] = house[up[0]][j-1]
    house[up[0]][up[1]+1] = 0

    # lower circle
    for i in range(down[0], R-1):
        house[i][0] = house[i+1][0]
    for j in range(C-1):
        house[R-1][j] = house[R-1][j+1]
    for i in range(R-1, down[0], -1):
        house[i][C-1] = house[i-1][C-1]
    for j in range(C-1, 0, -1):
        house[down[0]][j] = house[down[0]][j-1]
    house[down[0]][down[1]] = -1
    house[down[0]][down[1]+1] = 0


for time in range(T):
    spread()
    house = nxt
    nxt = [[0 for x in range(C)] for y in range(R)]

    #
    # print("spread")
    # for _ in house:
    #     print(*_)
    #
    circul()
    #
    # print("circulation")
    # for _ in house:
    #     print(*_)
    #

ans = 0
for i in range(R):
    for j in range(C):
        if house[i][j] >0:
            ans += house[i][j]

print(ans)

"""
8 8 10
7 6 5 4 3 2 1 2
8 0 0 0 0 0 0 3
9 0 0 0 0 0 0 4
-1 7 8 9 8 7 6 5
-1 7 8 9 8 7 6 5
9 0 0 0 0 0 0 4
8 0 0 0 0 0 0 3
7 6 5 4 3 2 1 2
"""

"""
138
"""