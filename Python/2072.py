import sys
input = sys.stdin.readline

N = int(input())


def checkEnd(i, j, wb):
    # horizontal
    row = grid[i][max(0, j-5):min(j+5, 20)]
    if checkFive(row, wb):
        return True
    col = [grid[x][j] for x in range(max(0, i-5), min(i+6, 20))]
    if checkFive(col, wb):
        return True
    diag = []
    for d in range(-5, 6):
        if 0 < i+d < 20 and 0 < j+d < 20:
            diag.append(grid[i+d][j+d])
    if checkFive(diag, wb):
        return True
    diag = []
    for d in range(-5, 6):
        if 0 < i-d < 20 and 0 < j+d < 20:
            diag.append(grid[i-d][j+d])
    if checkFive(diag, wb):
        return True

    return False


def checkFive(line, wb):
    combo = 0
    for l in line:
        if l == wb:
            combo += 1
        else:
            if combo == 5:
                return True
            combo = 0
    if combo == 5:
        return True
    return False


grid = [[0 for x in range(20)] for y in range(20)]  # 1: black ,-1: white

for turn in range(1, N+1):
    i, j = map(int, input().split())
    grid[i][j] = -1 if turn % 2 else 1

    if checkEnd(i, j, grid[i][j]):
        print(turn)
        break
else:
    print(-1)

"""
400*8*7*5
"""