import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dx = (2, -2, 0, 0)
dy = (0, 0, -2, 2)


chess_pieces = set()
cnt = set()
for _ in range(K):
    X, Y = map(int, input().split())
    chess_pieces.add((X, Y))


for x, y in chess_pieces:
    for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 1<=nx<=N and 1<=ny<=N and ((nx, ny) not in chess_pieces) and ((nx, ny) not in cnt):
                cnt.add((nx, ny))

print(len(cnt))
