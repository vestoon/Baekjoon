import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    three = 0
    while not N % 3:
        N //= 3
        three += 1

    if three > 1:
        print("TAK")
        continue
    if three == 1:
        print("NIE")
        continue

    if N % 3 == 1:
        print("NIE")
    else:
        print("TAK")
