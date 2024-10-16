import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = sys.maxsize

"""
부분합 충에 합이 S 이상이 되는 것 중 가장 짧은 것 구하기
높은 확률로 투 포인터
"""

acc = arr[0]
ans = sys.maxsize # 길이
i, j = 0, 0 # l = j-i+1
while True:
    if acc < S:
        j += 1
        if j == N: break
        acc += arr[j]
    else: # S <= acc
        ans = min(ans, j-i+1)
        acc -= arr[i]
        i += 1
        if j < i: break
        

print(ans if ans != sys.maxsize else 0)
