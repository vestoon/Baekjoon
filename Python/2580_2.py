import copy
sdoku = []
blank = []  # (i, j), possibilities 들어갈 수 있는 값의 인덱스가 True
for i in range(9):
    inp = list(map(int, input().split()))
    sdoku.append(inp)
    for j, num in enumerate(inp):
        if not num:
            blank.append((i, j))

sdoku_copy = [row[:] for row in sdoku]
# sdoku_copy = copy.deepcopy(sdoku)
# 3 x 3
block = [[[True for _ in range(10)] for x in range(3)] for y in range(3)]  # 사용할 수 있을 때 True
for i in range(9):
    for j in range(9):
        num = sdoku[i][j]
        if num:
            block[i//3][j//3][num] = False


def search(l, s):  # l 은 blank 의 index
    if l == len(blank):
        return s  # 기본 경우: 모든 빈 칸이 채워진 경우, 현재 보드 반환

    x, y = blank[l]
    pos = [True for _ in range(10)]  # x, y 에다 넣을 수 있는 숫자면 True
    pos[0] = False

    # 행 검사
    for n in s[x]:
        if pos[n]:
            pos[n] = False

    # 열 검사
    for n in range(9):
        if pos[s[n][y]]:
            pos[s[n][y]] = False

    # 블럭 검사
    for ni, n in enumerate(block[x // 3][y // 3]):
        if not n:
            pos[ni] = False

    # print(pos)
    for i, flag in enumerate(pos):
        if flag:
            # sc = copy.deepcopy(s)
            sc = [row[:] for row in s]
            sc[x][y] = i
            block[x//3][y//3][i] = False
            nxt = search(l+1, sc)
            if nxt:
                return nxt
            sc[x][y] = 0
            block[x // 3][y // 3][i] = True
    return False


ans = search(0, sdoku_copy)
for x in ans:
    for y in x:
        print(y, end=' ')
    print()


