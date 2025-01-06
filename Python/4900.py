import sys
input = sys.stdin.readline

"""
3글자씩 파싱해서 10진수로 저장(10씩 곱하면서)
변환한 두 숫자 더하기
다시 10씩 나누면서 변환하기
애초에 저장을 다 문자열로 해야 할듯?
"""


sev2dec = {}
dec2sev = {}
sev2dec["063"] = "0"
dec2sev["0"] = "063"

sev2dec["010"] = "1"
dec2sev["1"] = "010"

sev2dec["093"] = "2"
dec2sev["2"] = "093"

sev2dec["079"] = "3"
dec2sev["3"] = "079"

sev2dec["106"] = "4"
dec2sev["4"] = "106"

sev2dec["103"] = "5"
dec2sev["5"] = "103"

sev2dec["119"] = "6"
dec2sev["6"] = "119"

sev2dec["011"] = "7"
dec2sev["7"] = "011"

sev2dec["127"] = "8"
dec2sev["8"] = "127"

sev2dec["107"] = "9"
dec2sev["9"] = "107"

# 7 segment로 이루어진 문자열을 3 글자씩 변환해야 함
def parse(sev_long) -> str:
    ret = ""
    for i in range(0, len(sev_long), 3):
        tmp = sev_long[i:i+3]
        ret += sev2dec[tmp]
    return ret

# 10씩 나눠주면서 7세그먼트로 변환, 문자열로 반환
def serialization(dec_long: str) -> str:
    ans = ""
    for s in dec_long:
        ans += dec2sev[s]
    return ans


def sol(inp): # 뒤에  = 는 빠져 있다. 
    lValue, rValue = inp.split('+')
    dec_ret = int(parse(lValue)) + int(parse(rValue))

    return serialization(str(dec_ret))


while True:
    inp = input().rstrip()
    if inp == "BYE": break

    print(inp, end='')
    print(sol(inp[:-1]))



