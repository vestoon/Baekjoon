import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

# 3 x 3 단위로 사용한 수 검사하기
block = [[[False for _ in range(10)] for x in range(3)] for y in range(3)]  # 사용할 수 있을 때 True
row = [[False for x in range(10)] for r in range(9)] # row[i]: i번째 행에서 사용한 수
col = [[False for x in range(10)] for c in range(9)] # col[j]: j번재 열에서 사용한 수
for i in range(9):
    for j in range(9):
        num = board[i][j]
        if not num: continue
        block[i//3][j//3][num] = True
        row[i][num] = True
        col[j][num] = True


def simulation(cur) -> bool:  # l 은 blank 의 index
    if cur == 81:
        return True  # 기본 경우: 모든 빈 칸이 채워진 경우, 현재 보드 반환

    i, j = cur//9, cur%9
    if board[i][j]:
        return simulation(cur+1)
    
    for x in range(1, 10):
        if row[i][x] or col[j][x] or block[i//3][j//3][x]: continue
        board[i][j] = x
        row[i][x] = True
        col[j][x] = True
        block[i//3][j//3][x] = True

        if simulation(cur+1):
            return True
        
        board[i][j] = 0
        row[i][x] = False
        col[j][x] = False
        block[i//3][j//3][x] = False

    return False

if simulation(0):
    for line in board:
        print(*line)
else:
    print(-1)
