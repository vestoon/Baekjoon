N, r, c = map(int, input().split())
ans = 0

for n in range(N, 0, -1):
    mid = 2**(n-1)
    if r <= mid-1 and c <= mid-1:  # 1
        continue
    elif r <= mid-1 < c:  # 2
        ans += mid**2
        c -= mid
    elif c <= mid - 1 < r:  # 3
        ans += 2*(mid**2)
        r -= mid
    else:  # 4
        ans += 3*(mid**2)
        r -= mid
        c -= mid

print(ans)





