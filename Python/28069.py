from collections import deque

N, K = map(int, input().split())
# 이런 미친 문제... 제자리에서 무한정 제자리걸음이 가능하기 때문에 정확히 K번째까지 가지 않더라도 그 전에 찾았다면 프로그램을 종료해도 된다.


dp = [False for x in range(N+1)]
dp[0] = True
que = deque([0])

def sol():

    for _ in range(K):
        l = len(que)
        for __ in range(l):
            cur = que.popleft()
            if cur == N:
                return True
            dp[cur] = False
            a, b = cur+1, cur + cur//2
            if a <= N and not dp[a]:
                dp[a] = True
                que.append(a)
            if b <= N and not dp[b]:
                dp[b] = True
                que.append(b)
    
    return dp[N]

print("minigimbob" if sol() else "water")

# 1 2 3 4 5
# 0 1 2 3 4
# t t t f f