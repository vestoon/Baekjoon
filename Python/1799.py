import sys
input = sys.stdin.readline

"""
ans를 전역 변수로 두어야 나중에 가망이 없을 때 백트래킹으로 빠져나오기 수월하다.
"""

N = int(input())
ans = 0
right_down = [False for x in range(2*N-1)]
avaliable = [list(map(int, input().split())) for y in range(N)]


def upper_bound(d:int) -> int:
    ret = 0
    for d in range(d, 2*N - 1):
        for i in range(max(0, d- N+1), min(d+1, N)):
            j = d - i
            if avaliable[i][j] and not right_down[i-j]:
                ret += 1
                break
    return ret


def recur(d:int, acc:int):
    if d == 2*N - 1:
        global ans
        ans = max(ans, acc)
        return
    if acc + upper_bound(d) <= ans:
        return 

    for i in range(max(0, d- N+1), min(d+1, N)):
        j = d-i
        if not avaliable[i][j] or right_down[i-j]: continue

        right_down[i-j] = True
        recur(d+1, acc+1)
        right_down[i-j] = False
    recur(d+1, acc)

recur(0, 0)
print(ans)