N, M = map(int, input().split())

trees = tuple(map(int, input().split()))  # 나무들의 길이를 일일히 저장한 리스트
T = max(trees)
if T-M >= 0:
    a = T-M
else:
    a = 0
b = T
while b-a != 1:
    mid = (b+a)//2  # 중앙값 설정
    target = 0
    for tree in trees:
        if tree > mid:
            target += tree - mid
        if target >= M:
            a = mid
            break
    else:
        b = mid
    print(a, b)

print(a)
