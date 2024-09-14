# https://www.acmicpc.net/problem/21599
import sys
import heapq
input = sys.stdin.readline

N = int(input())
items = list(map(int, input().split()))
items.sort(reverse=True)
j = -1
for i in range(N):
    if items[i] == 0:
        break
    
    j = max(j, i-1 + items[i])

j = min(j, N-1)

print(j+1)