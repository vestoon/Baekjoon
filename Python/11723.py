import sys

M = int(sys.stdin.readline())
s = set()

for x in range(M):
    comnd = sys.stdin.readline().rstrip()
    # print('comnd:', comnd)

    if comnd == 'all':
        s = {x for x in range(1, 21)}
    elif comnd == 'empty':
        s = set()
    elif comnd[:2] == 'ad':
        x = int(comnd.split()[-1])
        if x not in s:
            s.add(x)
    elif comnd[:2] == 'ch':
        x = int(comnd.split()[-1])
        if x in s:
            print(1)
        else:
            print(0)
    elif comnd[:2] == 're':
        x = int(comnd.split()[-1])
        if x in s:
            s.remove(x)
    elif comnd[:2] == 'to':
        x = int(comnd.split()[-1])
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    # print('s:', s)
