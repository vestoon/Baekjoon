import math
import sys
N = int(input())

# 1 빼고 조화수열 계산하면 8~9 정도
M = 1 << (10**N)
bitPrime = 1  # 소수면 0이고 아니면 1 인걸로, 지금 전부 0으로 초기화된 상태

# 에라토스테네스의 체를 써서 걸러보자
for n in range(2, int(math.sqrt(10**N))):
    # point 의 배수를 싹 걸러낸다
    point = 1 << (n-1)
    # print(bin(point))

    if bitPrime & point:  # 이전 포인트에서 한번 걸렀다면 넘긴다
        # print('checked')
        continue
    print('n', n)

    point <<= n
    while point <= M:
        # print('point', point)
        bitPrime |= point
        point <<= n

# print(bin(bitPrime))
for testNum in range(10**(N-1), 10**N):
    org = testNum

    while testNum:
        if bitPrime & (1 << (testNum-1) ):
            break
        testNum //= 10
    else:
        print(org)
    # print(list_test)
print(sys.getsizeof(bitPrime))
