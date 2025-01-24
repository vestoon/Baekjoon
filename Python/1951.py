N = int(input())
MOD = 1234567
L = len(str(N))

"""
1 ~ N까지 몇 개의 활자가 필요한가?
결국은 자릿수 문제 

0 ~ 9

10 ~ 99

9
90
900
"""

acc = 0 # 출력해야 할 답
l = 1 # 현재 상태의 활자의 길이

while l < L:
    acc += l*9*(10**(l-1))
    acc %= MOD

    l += 1

acc += l*(N - (10**(l-1) - 1))
acc %= MOD
print(acc)
