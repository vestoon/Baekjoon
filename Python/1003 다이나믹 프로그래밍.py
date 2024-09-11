import sys

T = int(sys.stdin.readline())


def fibonacci(n):
    one = [0, 1]
    zero = [1, 0]
    if n <= 1:
        return zero[n], one[n]  # 알아서 튜플로 묶어준다
    else:
        for x in range(n-1):
            one.append(one[-1]+one[-2])
            zero.append(zero[-1] + zero[-2])
        return zero[-1], one[-1]


for x in range(T):
    n = int(sys.stdin.readline())
    for a in fibonacci(n):
        print(a, end=' ')




