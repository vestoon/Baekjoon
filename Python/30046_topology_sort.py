import sys
input = sys.stdin.readline

N = int(input())
P, Q, R = input().rstrip(), input().rstrip(), input().rstrip()
HJS_order = {'H':set(), 'J':set(), 'S':set()}
# P < Q < R 이어야 함

def HJS_test(a, b): # a -> b 로의 path가 존재하는지 확인 즉 a < b 인지 확인
    if a == b: return True

    for nxt in HJS_order[a]:
        if HJS_test(nxt, b):
            return True
    return False


PQ, QR, PR = False , False, False
for j in range(N):
    # print('j', j)
    p, q, r = P[j], Q[j], R[j]
    if p != q and not PQ: # p < q 여부 확인
        if HJS_test(q, p):
            print("Hmm...")
            break # 프로그램 종료
        else:
            HJS_order[p].add(q)
            PQ = True
    if q != r and not QR:
        if HJS_test(r, q):
            print("Hmm...")
            break
        else:
            HJS_order[q].add(r)
            QR = True
    if p != r and not PR:
        if HJS_test(r, p):
            print("Hmm...")
            break
        else:
            HJS_order[p].add(r)
            PR = True
    
    if PQ and QR:
        print("HJS! HJS! HJS!")
        break
else:
    print("Hmm...")
    

    
