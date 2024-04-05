import sys
n = int(sys.stdin.readline())
if not n:
    print(0)
    exit()


def cal(n):
    r = n - int(n)
    if r >= 0.5:
        return int(n)+1
    else:
        return int(n)


diffi = []
for _ in range(n):
    diffi.append(int(sys.stdin.readline()))

i = cal(n*0.15)
diffi.sort()

acc = 0
for x in diffi[i:n-i]:
    acc += x

print(cal(acc/(n-i*2)))

