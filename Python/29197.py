import sys
import math
input = sys.stdin.readline

gradient = set()
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    g = math.gcd(x, y)
    x //= g
    y //= g
    gradient.add((x, y))

print(len(gradient))




