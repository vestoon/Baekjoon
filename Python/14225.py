import sys
input = sys.stdin.readline

"""
수열의 부분 수열 중 만들 수 없는 가장 작은 수 구하기?
저장할 수 있는 배열은 일단 100,000까지만 만들어도 충분할 듯?
완탐은 2**20 정도?


이전 까지의 총합이란 지금까지의 값들로 만들 수 있는 최대값인데,
A[i]가 sum[:i]+1 이 아니라면 그 사이에 있는 수는 만들 수가 없다
"""

def sol():
    N = int(input()) # 1 <= N <= 20
    S = list(map(int, input().split())) # 1 <= Si <= 100,000
    canMake = [False for x in range(2000001)] # 0은 무시하자
    cal(0, 0, S, canMake)
    for x in range(1, 2000001):
        if not canMake[x]:
            print(x)
            break

def cal(i, acc, arr, canMake):
    if i == len(arr):
        return
    
    if acc+arr[i] < len(canMake):
        canMake[acc + arr[i]] = True

    cal(i+1, acc, arr, canMake)
    cal(i+1, acc+arr[i], arr, canMake)

sol()