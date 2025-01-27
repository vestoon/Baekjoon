import sys
input = sys.stdin.readline

N, M = map(int, input().split())
"""
M <= 10,000
블럭의 개수 M개로 만들 수 있는 직사각형은 정해져 있다.
어차피 2층에 있는 블럭은 전부 옮겨야 한다.

솔직히 완탐? 인가?
가능한 모든 직사각형 사이즈를 계산해서 
왼쪽 위부터 오른쪽 아래까지 전부 이동 거리 계산

100 100 100 10000
"""
block = [[0 for x in range(N+1)] for y in range(N+1)]

for _ in range(M):
    R, C = map(int, input().split())
    if not block[R][C]:
        block[R][C] = True

for i in range(1, N+1):
    block[i][0] += block[i-1][0]

for j in range(1, N+1):
    block[0][j] += block[0][j-1]

for i in range(1, N+1):
    for j in range(1, N+1):
        block[i][j] += block[i-1][j] + block[i][j-1] - block[i-1][j-1]

ans = M # 출력할 최소값값
for W in range(1, N+1):
    if M%W: continue
    # w, h : 직사각형의 가로, 세로
    H = M//W
    for i in range(1, N-H+2):
        for j in range(1, N-W+2):
            tmp = block[i+H-1][j+W-1] - block[i+H-1][j-1] - block[i-1][j+W-1] + block[i-1][j-1]
            ans = min(ans, M - tmp)


print(ans)

