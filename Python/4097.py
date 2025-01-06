import sys
input = sys.stdin.readline


"""
-3 4 9 -2 -5 8 2

dp[i] : i번째에서 끝나는 연속 부분 수열중 가장 가중치가 큰 값
"""



while True:
    N = int(input())
    if N == 0: break
    ans  = -sys.maxsize
    dp = [0 for x in range(N)]

    for i in range(N):
        P = int(input())
        if i == 0:
            ans = P
            dp[i] = P
            continue

        dp[i] = dp[i-1]+P if 0 < dp[i-1] else P
        ans = max(ans, dp[i])
    print(ans)



