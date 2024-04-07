import sys
N, M = map(int, sys.stdin.readline().split())

db = {}
for _ in range(N):
    add, pwd = sys.stdin.readline().split()
    db[add] = pwd

for _ in range(M):
    q = sys.stdin.readline().rstrip()
    print(db[q])

