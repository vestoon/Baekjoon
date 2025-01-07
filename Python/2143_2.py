import sys
import bisect
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
A_comb = [] # A의 부 배열의 합으로 만들 수 있는 모든 값 저장
cnt = 0

for i in range(n):
    tmp = 0
    for j in range(i, n):
        tmp += A[j]
        A_comb.append(tmp)
A_comb.sort()

for i in range(m):
    tmp = 0
    for j in range(i, m):
        tmp += B[j]
        l = bisect.bisect_left(A_comb, T - tmp)
        r = bisect.bisect_right(A_comb, T - tmp)
        cnt += r-l

# hash를 통해 구현
# print(comb)
print(cnt)