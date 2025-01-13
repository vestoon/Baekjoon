import sys
input = sys.stdin.readline

def match(left, right):
    l = min(len(left), len(right))
    for i in range(1, l+1):
        if left[-i:] == right[:i]:
            return True
        if right[-i:] == left[:i]:
            return True
    return False


cnt = 0
N = int(input())
names = [input().rstrip() for x in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if match(names[i], names[j]):
            # print(i, j)
            # print(names[i], names[j])
            # print()
            cnt += 1

print(cnt)