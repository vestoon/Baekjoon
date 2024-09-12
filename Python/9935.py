inp = input()
target = list(input())
ret = []
l = len(target)

for s in inp:
    ret.append(s)
    if ret[-l:] == target:
        del ret[-l:]

if ret:
    for x in ret:
        print(x, end="")
else:
    print("FRULA")
