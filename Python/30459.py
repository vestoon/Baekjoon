import sys
input = sys.stdin.readline

# N: 말뚝의 개수 2 <= N <= 2,000
# M: 깃대의 개수 1 <= M <= 40,000
# R: 현수막의 최대 넓이 1 <= R <= 1,000,000,000
N, M, R = map(int, input().split())

A = list(map(int, input().split())) # 말뚝의 위치 N 개 -20,000 <= A[i] <= 20,000
B = list(map(int, input().split())) # 깃대의 길이 M 가지 1 <= B[i] <= 40,000
A.sort()
B.sort()
ans = -1 # 현수막의 최대 넓이

"""
R 을 넘지 않는 A[i]*A[j]*R/2 의 최대값 구하기
완탐할 경우  2000 * 2000 * 40000 으로 무조건 시간 초과

모든 밑변 경우의 수 만들기 4,000,000, 실재 경우의 수는 40,000
밑변의 각 경우에 대해서 이분 탐색으로 높이를 탐색
4,000,000 + 40,000*(log2(40,000) = 15)
"""

widths = [False for x in range(40001)] # 가능한 모든 밑변의 길이
for i in range(N):
    for j in range(i+1, N):
        widths[A[j] - A[i]] = True

for w in range(1, 40001):
    if not widths[w]: continue

    # 이분 탐색 시작

    # 양 끝값에서의 예외 처리리
    if 2*R < B[0]*w: # 이 뒤로도 w는 계속 커지기 때문에 break
        break
    if B[-1]*w <= R*2:
        ans = B[-1]*w/2 # 현재 계산한 값 중 가장 큰 값인게 자명하다

    lo, hi = 0, M-1
    while lo+1 < hi:
        mid = (lo+hi)//2

        if w*B[mid] <= R*2:
            lo = mid
        else:
            hi = mid
    ans = max(ans, w*B[lo]/2)

print(ans)