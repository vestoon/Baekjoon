import sys
input = sys.stdin.readline

def contain(cx, cy, r, x, y) -> int:
    return abs(cx-x)**2 + abs(cy-y)**2 < r**2


T = int(input())
for tc in range(1, T+1):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0

    for _ in range(n):
        cx, cy, r = map(int, input().split())
        flag = 0
        if contain(cx, cy, r, x1, y1): flag += 1
        if contain(cx, cy, r, x2, y2): flag += 1
        if flag == 1:
            cnt += 1
    
    
    print(cnt)
