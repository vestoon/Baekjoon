import math
import array
import sys
N = int(input())

# 1 빼고 조화수열 계산하면 8~9 정도
M = 1 + 10**N
arrPrime = array.array('b', [True for x in range(M)])
arrPrime[1] = False

# 에라토스테네스의 체를 써서 걸러보자
for n in range(2, int(math.sqrt(M))):
    # point 의 배수를 싹 걸러낸다
    point = n
    if not arrPrime[point]:  # 이전 포인트에서 한번 걸렀다면 넘긴다
        continue

    point += n
    while point < M:
        # print('point', point)
        arrPrime[point] = False
        point += n

# for i, flag in enumerate(arrPrime):
#     print(i, ':', end=' ')
#     if flag:
#         print('Prime')
#     else:
#         print('not Prime')
for test_num in range(10**(N-1), 10**N):
    tn = test_num
    while tn:
        if not arrPrime[tn]:
            break
        tn //= 10
    else:
        print(test_num)
    # print(list_test)

# 메모리 확인
print('end', sys.getsizeof(arrPrime))
