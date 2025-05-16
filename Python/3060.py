import sys
input = sys.stdin.readline

T = int(input())

"""
돼지들의 요구상항이 어떤 상태이던지 결국에 요구사항의 총합은 하루가 지날 때마다 4배가 된다.
log4로 게산도 가능은 하겠지만 소수점 이슈로 인해 그냥 직접 계산하는 걸로
"""


# 6마리 돼지의 요구사항을 들어줄 수 없는 날이 몇 번째인지
for tc in range(1, T+1):
    N = int(input())
    cur_sum = sum(map(int, input().split()))

    day = 1
    while cur_sum <= N:
        cur_sum *= 4
        day += 1

    print(day)