# Second version
# Much more time and space
# But very short code
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

inp = []
while True:
    try:
        tmp = int(input())
        inp.append(tmp)
    except ValueError:
        break


def p2p(seq):
    if len(seq) == 1:
        print(seq[0])
        return

    root = seq[0]
    left = seq[1:]
    right = []
    for i in range(1, len(seq)):
        if seq[i] > root:
            right = seq[i:]
            left = seq[1:i]
            break

    if left:
        p2p(left)
    if right:
        p2p(right)
    print(root)


p2p(inp)
