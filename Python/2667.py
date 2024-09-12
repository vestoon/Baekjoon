N = int(input())
maze = []
visited = [[False for x in range(N)] for y in range(N)]
for x in range(N):
    maze.append(input())

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)


def dfs(x, y):
    count = 1
    visited[x][y] = True
    for g in range(4):
        near = (x + dx[g], y + dy[g])
        if (0 <= near[0] < N and 0 <= near[1] < N) and not visited[near[0]][near[1]] and maze[near[0]][near[1]] == '1':
            count += dfs(near[0], near[1])
    return count


ans = []
for i in range(N):
    for j in range(N):
        if maze[i][j] == '1' and not visited[i][j]:
            ans.append(dfs(i, j))


print(len(ans))
for x in sorted(ans):
    print(x)
