import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

even_sum, odd_sum = 0, 0
for i in range(N):
    if i%2: # 짝수 번째 
        even_sum += arr[i]
    else:
        odd_sum += arr[i]

if N == 3 and even_sum < odd_sum: # 예외
        print(-1)
else:
    print(abs(even_sum - odd_sum))