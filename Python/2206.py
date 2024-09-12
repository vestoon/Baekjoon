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

visited1 = [[False for x in range(M)] for y in range(N)]
visited2 = [[False for x in range(M)] for y in range(N)]
visited1[0][0] = True
visited2[0][0] = True
cnt = 1
findPath = False
que = collections.deque()
que.append((0, 0, False))  # 벽을 부순 적 있다면 True, 없다면 False
if N == 1 and M == 1:
    print(1)
    exit()

while que and not findPath:
    cnt += 1
    l = len(que)
    for _ in range(l):
        x, y, bk = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if bk and visited2[nx][ny]:
                continue
            if (not bk) and visited1[nx][ny]:
                continue
            if nx == N-1 and ny == M-1:
                findPath = True
                break
            if mp[nx][ny] == '0':
                que.append((nx, ny, bk))
                visited2[nx][ny] = True
                if not bk:
                    visited1[nx][ny] = True
            elif (not bk) and not visited2[nx][ny]:
                que.append((nx, ny, True))
                visited2[nx][ny] = True
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