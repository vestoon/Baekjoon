import sys
input = sys.stdin.readline

"""
키 글자수 단위로 해독한다. 아마 맵핑 하나만 만들면 될듯? 
가로세로도 맞춰 줘야 함
"""

key = input().rstrip()
encoded = input().rstrip()
w = len(key)
h = len(encoded)//w

idx = [(key[i], i) for i in range(len(key))]
idx.sort()

offset = 0
decoded1 = []
for col in range(h):
    tmp = [encoded[i+col] for i in range(0, len(encoded), h)]
    decoded1 += tmp

while offset < len(encoded):
    partition = decoded1[offset: offset+w]
    decoded = []
    for i in range(w):
        for j in range(w):
            if idx[j][1] == i:
                decoded.append(partition[j])
    for d in decoded:
        print(d, end='')

    offset += w
