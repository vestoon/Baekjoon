import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ans = 1
#dp[i] 는 i 에서부터의 가장 긴 증가하는 부분수열
dp = [0 for x in range(len(A))]
dp[-1] = 1

for i in range(len(A)-2, -1, -1):
    subMax = 0
    for ni in range(i+1, len(A)):
        if A[i] < A[ni]:
            subMax = max(subMax, dp[ni])

    dp[i] = subMax+1
    ans = max(ans, dp[i])

print(ans)
