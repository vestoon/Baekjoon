import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chickenHouses = []
houses = []
chickenDistance = 6250000

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            houses.append((i, j))
        elif tmp[j] == 2:
            chickenHouses.append((i, j))


def chooser(i, acc):
    if len(acc) == M:
        cd = 0
        global chickenDistance
        for h in houses:
            cdh = 100
            for ch in acc:
                cdh = min(cdh, abs(h[0] - ch[0]) + abs(h[1] - ch[1]))
            cd += cdh

        chickenDistance = min(chickenDistance, cd)
        return

    if i == len(chickenHouses):
        return
    chooser(i+1, acc + [chickenHouses[i]])
    chooser(i+1, acc)


chooser(0, [])
print(chickenDistance)