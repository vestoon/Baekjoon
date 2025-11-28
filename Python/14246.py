import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

"""
A[i: j+1]이 k보다 큰 모든 i,j 순서쌍의 개수 구하기
수열의 원소가 자연수이기 때문에 K를 넘어서는 순간 뒤쪽의 모든 경우의 수를 한 번에 더해서 계산한다.
"""

i, j = 0, 0
cur = arr[0]
ans = 0

while True:
    if k < cur:
        cur -= arr[i]
        i += 1
        # 이 뒤쪽의 모든 j가 전부 가능하다고 계산
        ans += n-j
    else:
        j += 1
        if j == n:
            break
        cur += arr[j]
    
print(ans)