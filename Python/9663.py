N = int(input())


vCol = [False for x in range(N)]
vDialSum = [False for x in range(2*N-1)]  # row + col 값 계산
vDialSub = [False for x in range(2*N-1)]  # 음수 인덱스 적용 row - col 값 계산


def dfs(r, c):
    if r == N-1:
        return 1
    ret = 0
    vCol[c] = True
    vDialSum[r+c] = True
    vDialSub[r-c] = True
    for nc in range(N):
        if not (vCol[nc] or vDialSub[r+1 - nc] or vDialSum[r+1 + nc]):
            ret += dfs(r+1, nc)

    vDialSub[r-c] = False
    vDialSum[r+c] = False
    vCol[c] = False

    return ret


acc = 0
for col in range(N):
    acc += dfs(0, col)

print(acc)
