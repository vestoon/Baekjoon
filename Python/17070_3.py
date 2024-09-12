# Third version
# Little faster
# Improved dp direction
import sys
input = sys.stdin.readline

N = int(input())

vertical = [[0 for x in range(N)] for y in range(N)]
horizontal = [[0for x in range(N)] for y in range(N)]
diagonal = [[0 for x in range(N)] for y in range(N)]
house = []
for _ in range(N):
    house.append(list(map(int, input().split())))

for col in range(1, N):
    if house[0][col]:
        break
    horizontal[0][col] = 1

for i in range(1, N):
    for j in range(2, N):
        if house[i][j]:
            continue

        if not house[i-1][j] and not house[i][j-1]:
            diagonal[i][j] = diagonal[i-1][j-1] + horizontal[i-1][j-1] + vertical[i-1][j-1]

        horizontal[i][j] = diagonal[i][j - 1] + horizontal[i][j - 1]
        vertical[i][j] = diagonal[i - 1][j] + vertical[i - 1][j]


print(vertical[N-1][N-1] + horizontal[N-1][N-1] + diagonal[N-1][N-1])

