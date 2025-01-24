import sys
input = sys.stdin.readline

"""
가장 긴 증가하는 부분 수열의 합 구하기!
"""

N = int(input())
scores = [int(input())]
dp = [scores[0]]

for i in range(N-1):
    score = int(input())
    tmp = score

    for j in range(i+1):
        if scores[j] < score:
            tmp = max(tmp, dp[j]+score)
    
    scores.append(score)
    dp.append(tmp)

print(max(dp))
