import sys
input = sys.stdin.readline

def power(a, b, c, d, e):
    # ret = a*(1+b/100)*((1-min(c, 1)) + min(c, 1)*d)*(1+e)
    ret = a*(100+b)*( 100*(100-min(c, 100)) + min(100, c)*d )*(100+e)
    return ret

a1, b1, c1, d1, e1 = map(int, input().split()) # 무기를 장착한 크리의 수치
a2, b2, c2, d2, e2 = map(int, input().split()) # 무기를 장착한 파부의 수치
a3, b3, c3, d3, e3 = map(int, input().split()) # 크리의 무기가 올려 주는 수치
a4, b4, c4, d4, e4 = map(int, input().split()) # 파부의 무기가 올려 주는 수치

tmp1 = power(a1, b1, c1, d1, e1) # 원래 크리의 상태 
tmp2 = power(a1-a3+a4, b1-b3+b4, c1-c3+c4, d1-d3+d4, e1-e3+e4) # 크리가 파부의 무기를 장착한 상태
if tmp1 < tmp2:
    print('+')
elif tmp1 == tmp2:
    print('0')
else:
    print('-')

tmp1 = power(a2, b2, c2, d2, e2)
tmp2 = power(a2-a4+a3, b2-b4+b3, c2-c4+c3, d2-d4+d3, e2-e4+e3)
if tmp1 < tmp2:
    print('+')
elif tmp1 == tmp2:
    print(0)
else:
    print('-')
