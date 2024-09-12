import sys
input = sys.stdin.readline

n = int(input())

dp = [0]
for _ in range(n):
    triangle = list(map(int, input().split()))
    tmp = []
    for i in range(0, len(triangle)):
        if i == 0:
            tmp.append(dp[i] + triangle[i])
        elif i == len(triangle)-1:
            tmp.append(dp[i-1] + triangle[i])
        else:
            tmp.append(max(dp[i-1], dp[i]) + triangle[i])

    dp = tmp

print(max(dp))