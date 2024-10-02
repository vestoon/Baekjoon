import sys
input = sys.stdin.readline

target = input().rstrip()
l = len(target)

N = int(input())
cnt = 0
for _ in range(N):
    ring = input().rstrip()
    ring += ring
    for i in range(10):
        if ring[i:i+l] == target:
            cnt  += 1
            break  

print(cnt)