import sys
input = sys.stdin.readline

def sigma(x):
    return x*(x+1)//2
"""
무조건 이전 점프보다 더 길게 뛰어야 한다. 
문제는 N이 10^16까지 간다는거
1+2+3+4+5+ 수열에서 특정 수를 뺀다면?

1에서 시작할 때
2에서 시작할 때
3에서 시작할 때

가짓수가 아닌 밟을 수 있는 가장 많은 징검다리의 수 구하기
최대한 촘촘하게 밟아야 한다. 
촘촘하게 밟다가 지나칠 수밖에 없는 구간이 생긴다

1~10 = 55
1~13 = 91
1~14 = 105
1~15 = 120

시그마 n < N < 시그마 n+1
x < N < x + n+1
sigma(cur) <= target

N-x < n+1

sigma(n) = (n+1)n / 2

결론 시그마 n으로 계속 더하다가 초과되는 지점이 있으면 1 빼주면 된다!


N = 10^16 일 때 최대값: 141421355 (약 1억 4천만)
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    lo, hi = 0, 141421356

    while lo + 1 < hi:
        mid = (lo+hi)//2

        if sigma(mid) <= N:
            lo = mid
        else:
            hi = mid
    print(lo)
