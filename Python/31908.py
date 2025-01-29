import sys
input = sys.stdin.readline

N = int(input())
couple = {}

for _ in range(N):
    p, s = input().split()
    if s == '-': continue

    if s not in couple:
        couple[s] = [p]
    else:
        couple[s].append(p)

ans = []
for k in couple:
    if len(couple[k]) == 2:
        ans.append(couple[k])

print(len(ans))
for a in ans:
    print(*a)
