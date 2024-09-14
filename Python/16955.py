# https://www.acmicpc.net/problem/16955
# 인덱스 처리하기가 너무나 귀찮고 범위도 작기 때문에 그냥 패딩을 해줌
board = [['O' for x in range(18)] for y in range(4)]
board += [['O' for x in range(4)] + list(input().rstrip()) + ['O' for x in range(4)] for x in range(10)] 
board += [['O' for x in range(18)] for y in range(4)]


def lineCheck(i, j, dy, dx):
    combo = 0

    for _ in range(9):
        if board[i][j] == 'X':
            combo += 1
            if combo == 5:
                return True
        else:
            combo = 0 
        i += dy
        j += dx

    return False

def check(i, j):
    board[i][j] = 'X'
    if lineCheck(i-4, j, 1, 0) or lineCheck(i, j-4, 0, 1): # 십자 방향으로 탐색
        return True
    if lineCheck(i-4, j-4, 1, 1) or lineCheck(i+4, j-4, -1, 1): # 대각선 방향으로 탐색
        return True

    board[i][j] = '.'
    return False


def sol():
    for i in range(4, 14):
        for j in range(4, 14):
            if board[i][j] == '.':
                if check(i, j):
                    return 1
    
    return 0

print(sol())