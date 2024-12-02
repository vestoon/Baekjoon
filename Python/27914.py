import sys
input = sys.stdin.readline

"""
일렬로 서 있는 N명의 학생들
연속한 위치에 있는 학생들을 인터뷰할 수 있음

'앞 X명의 학생들 중 연속한 몇 명을 골라 인터뷰를 할 때, 자신과 같은 학년의 학생이 한 명도 없도록 고르는 방법의 수 구하기?'
"""

N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
dp = [0 for x in range(N)]
dp[0] = 0 if A[0] == K else 1
combo = 1 if dp[0] else 0


for i in range(1, N):
    if A[i] == K:
        combo = 0
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + combo+1
        combo += 1

queries = list(map(int, input().split()))
for q in queries:
    print(dp[q-1])
