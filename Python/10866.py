import sys

N = int(sys.stdin.readline())
d = []

for x in range(N):
    comnd = sys.stdin.readline().rstrip()
    # print('comnd:', comnd)

    if comnd[:10] == 'push_front':
        d.insert(0, comnd.split()[-1])
    elif comnd[:9] == 'push_back':
        d.append(comnd.split()[-1])
    elif comnd == 'pop_front':
        if d:
            print(d.pop(0))
        else:
            print(-1)
    elif comnd == 'pop_back':
        if d:
            print(d.pop(-1))
        else:
            print(-1)
    elif comnd == 'size':
        print(len(d))
    elif comnd == 'empty':
        if d:
            print(0)
        else:
            print(1)
    elif comnd == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    elif comnd == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)
    # print('d:', d)

