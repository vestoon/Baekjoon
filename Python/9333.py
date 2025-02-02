import sys
input = sys.stdin.readline

# 10000로 나눈 뒤
def round(x: float):
    ret = x//10000
    if 5000 <= x%10000:
        ret += 1
    
    return ret


T = int(input()) # ~1000
for tc in range(1, T+1):
    R, B, M = input().split()
    """
    B: 빌린 돈 (센트)   ~500000
    R: 이자 (%)        ~50.00
    M: 과외비 (센트)    ~5000000
    """
    # 센트로 환산
    B = int(B[:-3]+B[-2:])
    M = int(M[:-3]+M[-2:])
    # 퍼센트도 소수점 없앰, 10000퍼센트
    R = int(R[:-3]+R[-2:])

    ans = 0
    while 0 < B:
        r = round(B*R)
        B += r
        B -= M

        ans += 1
        if ans == 1201:
            break

    print(ans if ans != 1201 else "impossible")
