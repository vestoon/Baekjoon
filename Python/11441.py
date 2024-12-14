import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
acc = []
last = 0
for a in A:
    acc.append(last+a)
    last += a
acc.append(0)


M = int(input())
for _ in range(M):
    i, j = map(int, input().split())

    print(acc[j-1] - acc[i-2])
