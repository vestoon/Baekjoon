import sys
input = sys.stdin.readline

N, M = map(int, input().split())

seq = list(map(int, input().split()))
seq = sorted(list(set(seq)))
N = len(seq)


def combination(acc, i):
    if len(acc) == M:
        print(*acc)
        return
    if len(acc) > M or i == N:
        return

    cases = [[seq[i]]*x for x in range(M, -1, -1)]
    for case in cases:
        combination(acc+case, i+1)


combination([], 0)
