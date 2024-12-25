import sys
input = sys.stdin.readline

S = input().rstrip()
l = len(S)
cards = {}
cnt = {}
for shape in 'PKHT':
    cards[shape] = [False for x in range(14)]
    cnt[shape] = 0

i = 0
while i < l:
    # print(cards)
    cur = S[i:i+3]
    s = cur[0]
    num = int(cur[1:])
    if cards[s][num]:
        print("GRESKA")
        exit()
    cards[s][num] = True
    cnt[s] += 1
    i += 3

for shape in "PKHT":
    print(13 - cnt[shape], end=' ')