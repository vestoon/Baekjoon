import sys
import heapq
input = sys.stdin.readline


# n개 배열 들어올 때마다 그냥 깡으로 합쳐서 싹 다 다시 정렬하기
N = int(input())
arr = list(map(int, input().split()))
for _ in range(N-1):
    arr += list(map(int, input().split()))
    arr.sort()
    arr = arr[N:]

print(arr[0])
# print(arr)