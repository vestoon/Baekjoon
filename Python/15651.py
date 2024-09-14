# https://www.acmicpc.net/problem/15651
N, M = map(int, input().split())

def sol(acc):
    if len(acc) == M:
        print(*acc)
        return

    for nxt in range(1, N+1):
        sol(acc+[nxt])

sol([])
