import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 1
    applies = [tuple(map(int, input().split())) for _ in range(N)]
    applies.sort()
    
    top = applies[0][1]
    for i in range(1, N):
        if applies[i][1] < top:
            cnt += 1
            top = applies[i][1]
    print(cnt)