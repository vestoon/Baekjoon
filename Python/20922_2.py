import sys
input = sys.stdin.readline

N, K = map(int, input().split())
left = 0
right = 0  # left <= i <= right, length = right-left + 1
ans = 0

a = list(map(int, input().split()))
cnt = [0 for x in range(N)]

# cnt 를 유동적으로 계산, 전체 수열에서의 카운트가 아니라 현재 l r 사이에서의 개수
while right != N:
    # print(cnt)
    if cnt[a[right]] > K:
        # print(left, right)
        cnt[a[left]] -= 1
        left += 1
        continue

    ans = max(ans, right - left + 1)
    right += 1
    if right == N:
        break
    cnt[a[right]] += 1   # right 는 처음 옮길 때 한 번만 증가해야 하는데 계속 증가시키고 있다

print(ans)

