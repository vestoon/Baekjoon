import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

for tc in range(1, T+1):
    log = input().rstrip()
    left, right = deque(), deque()

    for s in log:
        if s == '<':
            if left:
                right.appendleft(left.pop())
        elif s == '>':
            if right:
                left.append(right.popleft())
        elif s == '-':
            if left:
                left.pop()
        else:
            left.append(s)
    
    for s in left:
        print(s, end='')
    for s in right:
        print(s, end='')
    print()
