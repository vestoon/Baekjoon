n = int(input()) 

def is_pal(s: int) -> bool:
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l-i-1]:
            return False
    return True


def convert(num, base) -> str: # 어차피 팰린드롬 판정하는 건데 걍 뒤집어서 출력하자
    ret = ''
    while num:
        ret += str(num%base)
        num //= base
    
    return ret[::-1]

non = True
for b in range(2, 11):
    cb = convert(n, b)
    if is_pal(cb):
        non = False
        print(b, cb)

if non:
    print("NIE")