import sys
input = sys.stdin.readline

def dist(x1, y1, x2, y2) -> int:
    return abs(x1-x2) + abs(y1-y2)


N = int(input())
rooms = []
x0, y0, E0 = map(int, input().split())
visited = [[False for x in range(1001)] for y in range(1001)]


for _ in range(N):
    x, y, E = map(int, input().split())
    rooms.append((x, y, E))
    if visited[x][y]:
        exit()
    else:
        visited[x][y] = True


ans = 0
for x1, y1, e1 in rooms:
    power = max(0, E0 - dist(x1, y1, x0, y0))

    for x2, y2, e2 in rooms:
        power -= max(0, e2 - dist(x1, y1, x2, y2))
    
    ans = max(ans, power)

print(ans if ans else "IMPOSSIBLE")