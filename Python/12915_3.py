E, EM, M, MH, H = map(int, input().split())


def check(n):
    e, em, m, mh, h = E, EM, M, MH, H
    if e < n:
        if em < n-e:
            return False
        em -= n-e
    if h < n:
        if mh < n-h:
            return False
        mh -= n-h
    if m < n:
        return n-m <= mh+em
    return True


lo = 0
# hi = max(E, M, H)+max(MH, EM)+1
hi = 300000
# print(check(lo))
# print(check(hi))
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid):
        lo = mid
    else:
        hi = mid

print(lo)
