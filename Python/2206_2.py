import sys
import collections
input = sys.stdin.readline

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

mp = []
walls = []  # (d, x, y)
N, M = map(int, input().split())
for _ in range(N):
    line = input()
    mp.append(line)

visited = [[[False, False] for x in range(M)] for y in range(N)]
visited[0][0][0] = True
cnt = 1
findPath = False
que = collections.deque()
que.append((0, 0, 0))  # 벽을 부순 적 있다면 True, 없다면 False
if N == 1 and M == 1:
    print(1)
    exit()

while que and not findPath:
    cnt += 1
    l = len(que)
    for _ in range(l):
        x, y, z = que.popleft()
        # print(x, y, z)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않고
            if 0 > nx or 0 > ny or N <= nx or M <= ny or visited[nx][ny][z]:
                continue
            if nx == N-1 and ny == M - 1 :
                findPath = True
                break
            if mp[nx][ny] == '0':
                que.append((nx, ny, z))
                visited[nx][ny][1] = True
                if z == 0:
                    visited[nx][ny][0] = True
            elif z == 0:
                que.append((nx, ny, 1))
                visited[nx][ny][1] = True
        if findPath:
            break

print(cnt) if findPath else print(-1)

# 벽을 부수지 않고 도착한 거리와 벽을 부수고 도착한 거리의 최소값 구하기?  or  벽을 부순 경우와 그렇지 않은 경우의 visited를 따로 만들기?
# visited1: 벽을 한 번도 부수지 않은 원소 가 방문한 길
# visited2: 벽을 한 번 부숴버린 원소가 지나간 길
# 벽을 한 번도 부수지 않은 경우: visited1 일 때만 진입
# 벽을 한 번 부순 경우: visited2 먼저 확인하고 방문시 방문하지 않음, 암튼 둘다 방문 안해야 함

"""
9 9
010001000
010101010
010101010
010101010
010101010
010101010
010101010
010101011
000100010

33
"""