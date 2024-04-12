import sys
 
N, M = map(int, sys.stdin.readline().split())

nothear = set()
notsee = set()
for h in range(N):
    person = sys.stdin.readline().rstrip()
    nothear.add(person)

for s in range(M):
    person = sys.stdin.readline().rstrip()
    notsee.add(person)

ans = sorted(nothear & notsee)
print(len(ans))
for x in ans:
    print(x)

