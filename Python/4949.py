import sys

def balance(string, end):
    i = 0  # index
    se = {'(': ')', '[': ']'}
    print('string =', string)
    print('end =', end)

    while i < len(string):  # i 를 증가시키면서 string[i] 비교하기
        if string[i] in se:  # 시작기호를 만났을 때
            print('recursion start')
            rest = balance(string[i+1:], se[string[i]])
            if rest:
                i += rest+1
            else:
                print('False')
                return False
        elif string[i] in {'.', ')', ']'}:  # 종료기호 중 하나를 만났을 때
            print('recursion end with', string[i])
            if string[i] == end:
                print('end normally')
                print('return',i+1)
                return i + 1
            else:
                print('end expression is incorrect')
                print('False')
                return False
        else:  # 그냥 일반 문자열들
            i += 1
    else:
        return False  # 종료 문구가 안나왔을 경우
    #   (()((()()()(((({}((}){(}){}.
# ex = "(()((()()()(((({}((}){(}){}."
#
# print(balance(ex, '.'))  # 결과는 123456789다? 인덱스 계산이 잘못돼서 젤 마지막을 뛰어넘은듯
# print('correct answer is', len(ex))

while True:
    inp = sys.stdin.readline().rstrip()
    if inp == '.':
        break
    else:
        if balance(inp, '.'):
            print('yes')
        else:
            print('no')



