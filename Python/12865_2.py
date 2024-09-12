import sys
input = sys.stdin.readline


N, K = map(int, input().split())

dp = [0 for x in range(K+1)]
objects = []
for _ in range(N):
    W, V = map(int, input().split())
    objects.append((W, V))


for obj in objects:
    w, v = obj
    for k in range(K, 0, -1):
        if dp[k] == 0:
            continue
        if k + w > K:
            continue

        dp[k+w] = max(dp[k+w], dp[k] + v)

    if w <= K:
        dp[w] = max(dp[w], v)

print(max(dp))

