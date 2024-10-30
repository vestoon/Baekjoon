import sys
input = sys.stdin.readline


width, height = map(int, input().split())
cnt = int(input())
row, col = [], []
maxArea = 0

for _ in range(cnt):
    direction, i = map(int, input().split())
    if direction:
        col.append(i)
    else:
        row.append(i)
row.sort()
col.sort()

prev = 0
rowPieces, colPieces = [], []
for r in row:
    rowPieces.append(r-prev)
    prev = r
rowPieces.append(height - prev)
prev = 0
for c in col:
    colPieces.append(c - prev)
    prev = c
colPieces.append(width - prev)

for w in rowPieces:
    for h in colPieces:
        maxArea = max(maxArea, w*h)

print(maxArea)
