import sys
K = int(sys.stdin.readline())
stack = []
for g in range(K):
    inp = int(sys.stdin.readline())
    if not inp:
        stack.pop(-1)
    else:
        stack.append(inp)

print(sum(stack))

