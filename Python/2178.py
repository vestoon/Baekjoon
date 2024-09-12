import collections
import sys
N, M = map(int, sys.stdin.readline().split())
maze = []
visited = [[False for x in range(M)] for y in range(N)]
visited[0][0] = True
for line in range(N):
    tmp = list(sys.stdin.readline().rstrip())
    tmp = list(map(int, tmp))
    maze.append(tmp)

# #
# print('maze')
# for x in maze:
#     print(x)
# #
q = collections.deque()
q.append(0)
q.append((0, 0))
level = 0

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

front = 0
while front != (N-1, M-1):
    front = q.popleft()
    # print('front', front)
    if not front:
        # print('level:', level)
        level += 1
        q.append(0)
        continue

    for i in range(4):
        near = (front[0]+dx[i], front[1]+dy[i])
        if (0 <= near[0] < N and 0 <= near[1] < M) and not visited[near[0]][near[1]] and maze[near[0]][near[1]]:
            visited[near[0]][near[1]] = True
            q.append(near)


print(level)
