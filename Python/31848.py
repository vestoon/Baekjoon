import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
ans = [0 for x in range(100001)] # 구멍의 크기 별로 어느 구멍에 들어가는지
ans[0] = 1

for i in range(N):
    # 구멍 번호는 i+1 이다
    size = a[i] + i
    size = min(size, 100000)

    while not ans[size]:
        ans[size] = i+1
        size -= 1
    

Q = int(input())
s = list(map(int, input().split()))
for query in s:
    print(ans[query], end=' ')



