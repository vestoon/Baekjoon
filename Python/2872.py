import sys
input = sys.stdin.readline

N = int(input())
books = []
nxt = N

for x in range(N):
    n = int(input())
    books.append(n)

for i in range(N-1, -1, -1):
    if books[i] == nxt:
        nxt -= 1

print(nxt)
