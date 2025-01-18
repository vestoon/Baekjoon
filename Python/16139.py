import sys
input = sys.stdin.readline

def encode(s):
    return ord(s) - ord('a')

S = input().rstrip()
L = len(S)
q = int(input())

# 문자열 별로 누적 합 계산
acc = [[0] for x in range(26)]

for s in S:
    es = encode(s)
    for i in range(26):
        if es == i:
            acc[i].append(acc[i][-1]+1)
        else:
            acc[i].append(acc[i][-1])

for _ in range(q):
    # 인덱스는 0부터
    # l <= x <= r 에서 a 의 개수 구하기
    inp = input().split()
    a = inp[0]
    ea = encode(a)
    l, r = map(int, inp[1:])
    print(acc[ea][r+1] - acc[ea][l])

# for z in acc:
#     print(*z)