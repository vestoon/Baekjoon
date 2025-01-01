import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
ans = 0
prev = 0

for h in H:
    ans += 2*h + 2 + abs(h-prev)
    prev = h

ans += prev
print(ans)
