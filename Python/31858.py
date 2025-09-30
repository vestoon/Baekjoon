import sys
from collections import deque
input = sys.stdin.readline

"""
오큰수라기보단 monotone stack을 사용하는 문제
스택 내부가 오름차순으로 정렬되어 있다는 사실을 명심하자
"""

N = int(input())
arr = list(map(int, input().split()))

LGE = [-1 for x in range(N)]
st = deque()
ans= 0

# (i, j) 탐색
for i in range(N-1, -1, -1):
  # j 찾기
  cur = arr[i]
  while st and st[0] < cur:
    # min(arr[i], arr[j]) = arr[j] 이면서 조건을 만족하는 경우
    # i와 j 사이에 있었을 값들은 arr[j]보다 작다는 것이 보장된다.
    ans += 1
    st.popleft()
  
  if st:
    # min(arr[i], arr[j]) = arr[i] 이면서 조건을 만족하는 경우
    # arr[i] < arr[j]이기 때문에 j 보다 오른쪽에 있는 값들은 j에 의해서 조건을 만족하지 못한다.
    ans += 1
  st.appendleft(cur)
  
print(ans)
