import sys
import collections
input = sys.stdin.readline

N = int(input())
last = 0
q = collections.deque()
order = collections.deque()

for _ in range(N):
    cmd = input().split()
    c = cmd[0]

    if c == '1':
        q.append(cmd[1])
        order.append(1)
    elif c == '2':
        q.appendleft(cmd[1])
        order.append(-1)
    elif c == '3' and q:
        o = order.pop()
        if o == 1:
            q.pop()
        else:
            q.popleft()

if q:
    while q:
        print(q.popleft(), end='')
else:
    print(0)

