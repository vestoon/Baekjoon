import sys

N, M = map(int, sys.stdin.readline().split())
paper = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    paper.append(line)
ans = 0


def tet_2x3(src):  # (i,j) 영역의 제일 왼쪽 위 좌표
    global ans
    for x in range(6):
        for y in range(x+1, 6):
            fst = (x // 3, x % 3)  # 투포인터?
            sec = (y // 3, y % 3)  # 제외해야할 두 개의 좌표
            if fst[1] == sec[1]:  # 아래로 기둥
                continue
            elif fst[0] != sec[0] and fst[1] + 1 == sec[1]:  # 오른쪽 아래
                continue
            elif fst[0] != sec[0] and fst[1] - 1 == sec[1]:  # 왼쪽 아래
                continue

            acc = 0
            # 이걸 통과하는 8가지 경우의 수에 대해서
            for i in range(2):
                for j in range(3):
                    dxdy = (i, j)
                    if dxdy == fst or dxdy == sec:
                        continue
                    nx = src[0] + dxdy[0]
                    ny = src[1] + dxdy[1]
                    acc += paper[nx][ny]

            if acc > ans:
                ans = acc


def tet_3x2(src):
    global ans
    for x in range(6):
        for y in range(x+1, 6):
            fst = (x // 2, x % 2)
            sec = (y // 2, y % 2)
            if fst[0] == sec[0]:  # 옆으로 기둥
                continue
            elif fst[0] + 1 == sec[0] and fst[1] + 1 == sec[1]:
                continue
            elif fst[0] + 1 == sec[0] and fst[1] - 1 == sec[1]:
                continue

            acc = 0
            for i in range(3):
                for j in range(2):
                    dxdy = (i, j)
                    if dxdy == sec or dxdy == fst:
                        continue
                    nx = src[0] + dxdy[0]
                    ny = src[1] + dxdy[1]
                    acc += paper[nx][ny]

            if acc > ans:
                ans = acc


def tet_2x2(src):
    global ans
    acc = 0
    for i in range(2):
        for j in range(2):
            nx = src[0] + i
            ny = src[1] + j
            acc += paper[nx][ny]

    if acc > ans:
        ans = acc


def tet_4x1(src):
    global ans
    acc = 0
    for n in range(4):
        acc += paper[src[0]+n][src[1]]

    if acc > ans:
        ans = acc


def tet_1x4(src):
    global ans
    acc = 0
    for n in range(4):
         acc += paper[src[0]][src[1]+n]

    if acc > ans:
        ans = acc


for i in range(N-1):
    for j in range(M-2):
        tet_2x3((i, j))

for i in range(N-2):
    for j in range(M-1):
        tet_3x2((i, j))

for i in range(N-1):
    for j in range(M-1):
        tet_2x2((i, j))

for i in range(N):
    for j in range(M-3):
        tet_1x4((i, j))

for i in range(N-3):
    for j in range(M):
        tet_4x1((i, j))

print(ans)







