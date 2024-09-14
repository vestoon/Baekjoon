import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    cnt5 = 0

    cur5 = 5
    
    while cur5 <= N:
        cnt5 += N//cur5
        cur5 *= 5
    
    print(cnt5)

    