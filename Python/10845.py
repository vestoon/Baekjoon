import sys

N = int(sys.stdin.readline())
q = []

for x in range(N):
    comnd = sys.stdin.readline().rstrip()
    # print('cmond:', comnd)

    if comnd == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)
    elif comnd == 'size':
        print(len(q))
    elif comnd == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif comnd == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif comnd == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    else:
        q.append(comnd.split()[-1])
    # print('q:', q)
