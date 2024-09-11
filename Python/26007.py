import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

delta = list(map(int, input().split()))
acc = [0]
a = 0

for d in delta:
    X += d
    if X < K:
        a += 1
    acc.append(a)

# print(acc)
for _ in range(M):
    l, r = map(int, input().split())
    print(acc[r-1] - acc[l-1])
