sdoku = []
blank = []  # (i, j), possibilities 들어갈 수 있는 값의 인덱스가 True
for i in range(9):
    inp = list(map(int, input().split()))
    sdoku.append(inp)
    for j, num in enumerate(inp):
        if not num:
            blank.append((i, j))

# 3 x 3
block = [[[True for _ in range(10)] for x in range(3)] for y in range(3)]  # 사용할 수 있을 때 True
for i in range(9):
    for j in range(9):
        num = sdoku[i][j]
        if num:
            block[i//3][j//3][num] = False


def search(l):  # l 은 blank 의 index
    global sdoku
    if l == len(blank):
        return sdoku
    print('l:', l, blank[l])
    x, y = blank[l]
    pos = [True for x in range(10)]  # x, y 에다 넣을 수 있는 숫자면 True

    # 행 검사
    for n in sdoku[x]:
        if pos[n]:
            pos[n] = False

    # 열 검사
    for n in range(9):
        if pos[sdoku[n][y]]:
            pos[sdoku[n][y]] = False

    # 블럭 검사
    for ni, n in enumerate(block[x // 3][y // 3]):
        if not n:
            pos[ni] = False

    print('pos:', pos)
    for x in pos:  # l 번 빈칸에 넣을 숫자가 없을 때는 False 를 리턴
        if x:
            break
    else:
        return False

    for i, flag in enumerate(pos):
        print('i:', i)
        if not i:  # 0은 안씀
            continue
        if flag:
            sdoku[x][y] = i
            #
            # for _ in sdoku:
            #     print(_)
            #
            block[x//3][y//3][i] = False
            if search(l+1):
                return sdoku
            print('??', l)
            sdoku[x][y] = 0
            block[x//3][y//3][i] = True


for x in block:
    print(x)
print(search(0))
for x in sdoku:
    print(x)
for x in block:
    print(x)
