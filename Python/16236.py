import sys
import collections
input = sys.stdin.readline

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)

N = int(input())
space = []
start = [0, 0]
exp = 0  # number of fish baby shark ate
level = 2  # size of baby shark
ans = 0


def bfs(i, j):  # if you can't find, return -1
    visited = [[False for x in range(N)] for y in range(N)]
    q = collections.deque()
    q.append((i, j))
    visited[i][j] = True
    dist = 0
    while q:
        l = len(q)
        nxts = sorted([q.popleft() for x in range(l)])
        for front in nxts:
            y, x = front
            # print(y, x)
            global exp, level
            if 0 < space[y][x] < level:

                start[0] = y
                start[1] = x
                space[y][x] = 0  # eat
                exp += 1
                if exp == level:  # level up
                    level += 1
                    exp = 0
                return dist

            for n in range(4):
                ny, nx = y + dy[n], x + dx[n]
                if 0 <= ny < N and 0 <= nx < N and space[y][x] <= level and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True

        dist += 1

    return -1


for i in range(N):
    line = list(map(int, input().split()))

    for j in range(N):
        if line[j] == 9:
            line[j] = 0
            start = [i, j]

    space.append(line)


d = bfs(start[0], start[1])
while d != -1:
    ans += d
    d = bfs(start[0], start[1])

print(ans)
