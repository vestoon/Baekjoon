import sys
N = int(input())
grid = [input().rstrip() for x in range(N)]
cnt = 0
vector = [(1, 1), (1, -1), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

def inRange(i, j):
    return 0<=i<N and 0<=j<N

def countMobis(i, j):
    global cnt

    for v in vector:
        
        for d in range(1, 5):
            ni, nj = i+v[0]*d, j+v[1]*d 
            if not inRange(ni, nj) or grid[ni][nj] != "MOBIS"[d]:
                break
        else:
            cnt += 1

for i in range(N):
    for j in range(N):
        if grid[i][j] == "M":
            countMobis(i, j)

print(cnt)