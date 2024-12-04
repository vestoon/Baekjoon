import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

"""
각 a를 기준으로 a 보다 오른쪽에 a보다 작은 b가 몇 개나 있는지를 세는 문제

모든 i 에 대하여 b <= a 이고 B는 오름차순 정렬이 되어 있다. 
그냥 이분탐색 하면 되는 거 아닌가?
"""

def check(i, cmp):
    if i == N:
        return False
    return B[i] <= cmp

# i 번째 인덱스부터 끝까지 이분탐색 하기
def bisect(i):
    lo = i
    hi = N

    while lo+1 < hi:
        mid = (lo+hi)//2

        if check(mid, A[i]):
            lo = mid
        else:
            hi = mid
    
    return hi

for i in range(N):
    print(bisect(i)-i-1, end=' ')
