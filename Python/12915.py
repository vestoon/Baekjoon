E, EM, M, MH, H = map(int, input().split())
ans = -1

for a1 in range(EM+1):
    mh = MH
    e, m, h = E+a1, M+EM-a1, H

    if m < h:
        if h-m < mh:
            mh -= h-m
            m += h-m
            m += mh//2
            h += mh//2  # Don't care remainder
        else:
            m += mh
    elif h < m:
        if m - h < mh:
            mh -= m-h
            h += m-h
            m += mh//2
            h += mh//2
        else:
            h += mh
    else:
        m += mh//2
        h += mh//2

    # cur = min(e, m, h)
    # if ans < cur:
    #     print('a1', a1)
    #     # print(e, m, h)
    #     print(mh)
    #     print("!!!!!!!111", cur)
    #     ans = cur
    ans = max(ans, min(e, m, h))

print(ans)
