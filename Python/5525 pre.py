import sys
N = int(sys.stdin.readline())  # 부분 문자열의 'O' 의 개수
M = int(sys.stdin.readline())  # S 의 길이
S = sys.stdin.readline().rstrip()


pre = 'O'  # 이전 값
combo = 0  # 연속된 IOI 에서 I의 개수
count = 0
for x in S:
    if x != pre:  # 콤보가 이어지는 경우
        if x == 'I':
            combo += 1
    else:  # 이전 값이랑 같아서 콤보가 끊어지는 경우
        if combo - 1 >= N:
            count += combo - N
        combo = 0 if x == 'O' else 1
    pre = x
if combo - 1 >= N:
    count += combo - N

print(count)
