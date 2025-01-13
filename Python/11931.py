import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for x in range(N)]
arr.sort(reverse=True)

for a in arr:
    print(a)