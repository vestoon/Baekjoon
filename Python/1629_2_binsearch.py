import random

# A를 B 번 곱한 값을 C 롤 나눈 값을 알아보자
A, B, C = map(int, input().split())

# A = int(random.random()*20+1)
# B = int(random.random()*20+1)
# C = int(random.random()*20+1)

# print(A, B, C)


def cal(a, b):
    # print('b', b)
    if b == 1:
        return a % C

    sub = cal(a, b//2)
    sub = (sub*sub) % C
    if b % 2:
        sub = (sub*a) % C

    # print('ret', sub)
    return sub


A %= C
print(cal(A, B))
