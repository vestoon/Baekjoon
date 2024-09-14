import sys
input = sys.stdin.readline
from collections import deque

"""
어디서부터 비교해야 하는지 유효 범위를 알아야 함

where : A의 어느 위치의 값과 대응되는지 저장
B[j]의 왼쪽에 있는 where이 있는 값 중에서 가장 B[j]보다 큰 가장 가까운 값을 찾는다
찾는 중에 
그 값의 where 값부터 시작해서 A에 일치하는 값이 있는지 탐색
있다면 where에 저장, 가까운 값부터 자기까지의 where을 모두 -1로 초기화해야 한다

"""

N = int(input())
A = list(map(int, input().split()))
visited = [False for x in range(N)]
M = int(input())
B = list(map(int, input().split()))
where = [-1 for x in range(M)]
LCS = deque()

# i = 0 # A에서의 탐색 시작 지점??
for j in range(M):
    flag = j-1 # 가장 가까운 값
    while 0 <= flag and (B[flag] < B[j] or where[flag] == -1):
        flag -= 1

    for i in range(where[flag]+1, N):
        if A[i] != B[j]: # 이미 사용한 수거나 애초에 같지 않으면 continue
            continue 

        # B[j]보다 같거나 큰 값을 찾아서 왼쪽으로
        where[j] = i
        for k in range(flag+1, j):
            where[k] = -1
        break

# print(where)
ans = []
cnt = 0
for j in range(M):
    if where[j] != -1:
        cnt += 1
        ans.append(B[j])
print(cnt)
print(*ans)