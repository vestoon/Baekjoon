# Second version
# Less memory & less time
# Sort the numbers first
N, M = map(int, input().split())

seq = sorted(list(map(int, input().split())))
visited = [False for _ in range(N)]
subseq = []


def dfs():
    if len(subseq) == M:
        print(*subseq)
        return

    prv = 0
    for i in range(N):
        if seq[i] == prv or visited[i]:
            continue

        subseq.append(seq[i])
        visited[i] = True
        dfs()
        visited[i] = False
        subseq.pop()
        prv = seq[i]


dfs()
