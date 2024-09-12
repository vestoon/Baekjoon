import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    sticker = []
    for _ in range(2):
        tmp = tuple(map(int, input().split()))
        sticker.append(tmp)
    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue

    dp = [[0 for x in range(n+1)] for y in range(2)]
    # [0][0]
    dp[1][1] = sticker[0][0]
    # [0][1]
    dp[1][2] = sticker[0][1]+sticker[1][0]
    # [1][0]
    dp[0][1] = sticker[1][0]
    # [1][1]
    dp[0][2] = sticker[0][0] + sticker[1][1]

    for i in range(1, n):
        dp[0][i+1] = max(dp[0][i+1], dp[1][i] + sticker[1][i])
        dp[1][i+1] = max(dp[1][i+1], dp[0][i] + sticker[0][i])

        if i != n-1:
            dp[1][i+2] = max(dp[1][i+2], dp[1][i] + sticker[1][i] + sticker[0][i+1])
            dp[0][i+2] = max(dp[0][i+2], dp[1][i] + sticker[1][i+1])

            dp[1][i+2] = max(dp[1][i+2], dp[0][i] + sticker[0][i+1])
            dp[0][i+2] = max(dp[0][i+2], dp[0][i] + sticker[0][i] + sticker[1][i+1])

    print(max(dp[0][-1], dp[1][-1]))


