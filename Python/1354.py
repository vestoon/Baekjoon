"""
P가 2 이상이면 어차피 0을 수렴하는 속도가 log일 텐데 그냥 재귀로 깡 구현하면 괜찮지 않을까?
"""
N, P, Q, X, Y = map(int, input().split())
dp = {}

def A(x):
    if x <= 0:
        return 1
    if x in dp:
        return dp[x]
    
    ret = A(int(x/P) - X) + A(int(x/Q) - Y)
    dp[x] = ret

    return ret

print(A(N))