import sys
T = int(sys.stdin.readline())


def mod(x, n):
    return x % n if x % n else n


for test in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())

    start = mod(x, N)  # y를 찾을 때까지 이 수에다가 M을 더함

    if y == start:  # 첫 번째 사이클에서 바로 찾을 경우
        print(x)
        continue
    point = mod(start+M, N)

    cycle = 2
    while point != start:  # 처음 값을 다시 찾기 전까지
        if point == y:
            print((cycle - 1)*M + x)
            break
        cycle += 1
        point = mod(point+M, N)
    else:
        print(-1)

