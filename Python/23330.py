import sys
input = sys.stdin.readline

N = int(input())
points = list(map(int, input().split()))
points.sort()
ans = 0
if N == 1:
    print(0)
    exit()

for i in range(1, N):
    ans += (points[i]-points[i-1])*i*(N-i)

print(ans*2)

"""
1 4x1
2 3x2
3 2x3
4 1x4

"""