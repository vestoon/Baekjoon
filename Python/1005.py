import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline


def dfs(n):
    if not adj_list[n]:
        return con_time[n]

    if total_time[n] != -1:
        return total_time[n]

    ret = []
    for prev in adj_list[n]:
        ret.append(dfs(prev))

    ret = max(ret) + con_time[n]
    total_time[n] = ret
    return ret


T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    con_time = [0] + list(map(int, input().split()))
    total_time = [-1 for x in range(N+1)]
    adj_list = [[] for x in range(N+1)]

    for _ in range(K):
        prev, nxt = map(int, input().split())
        adj_list[nxt].append(prev)

    dst = int(input())

    print(dfs(dst))

