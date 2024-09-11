import sys
import collections
n, m = map(int, sys.stdin.readline().split())  # n:세로, m:가로
M = []
ans = []
for x in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    ans_row = []
    for y in range(m):
        dot = line[y]
        if dot == 2:
            dst = (x, y)
            ans_row.append(0)
        elif dot == 1:
            ans_row.append(-1)
        else:
            ans_row.append(0)
    M.append(line)
    ans.append(ans_row)


visited = [[False for x in range(m)] for y in range(n)]
# visited[dst[0]][dst[1]] = True
# print(visited)
distance = 1
dq = collections.deque()
dq.append(dst[0])
dq.append(dst[1])
dq.append(-1)
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
# print(dst)

while len(dq) != 1:
    x = dq.popleft()
    if x == -1:
        distance += 1
        dq.append(-1)
    else:
        y = dq.popleft()
        # print('x, y:', x, y, 'and', distance)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < m) and (not visited[nx][ny]):
                visited[nx][ny] = True
                if ans[nx][ny] == -1:
                    ans[nx][ny] = distance
                    dq.append(nx)
                    dq.append(ny)

for x in ans:
    for y in x:
        print(y, end=' ')
    print()
