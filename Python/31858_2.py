import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
ans = N-1
arr = list(map(int, input().split()))
lgn = [-1 for x in range(N)] # 왼큰수
rgn = [-1 for x in range(N)] # 오큰수

st = deque()

# 오큰수 구하기
for i in range(N-1, -1, -1):
    if not st:
        st.appendleft(i)
        continue

    while st:
        cmp = st.popleft()
        # cmp 가 더 작다면 버려야 함

        # 하지만 크다면 둘 다 넣어야 함
        if arr[i] < arr[cmp]:
            rgn[i] = cmp
            st.appendleft(cmp)
            st.appendleft(i)
            break
    else:
        st.appendleft(i)
    # break 되지 않았다면 기본적으로 -1

st = deque()
# 왼큰수 구하기
for i in range(N-1):
    if not st:
        st.append(i)
        continue

    while st:
        cmp = st.pop()

        if arr[i] < arr[cmp]:
            lgn[i] = cmp
            st.append(cmp)
            st.append(i)
            break
    else:
        st.append(i)


# print(*rgn)
# print(*lgn)
for i in range(N):
    if lgn[i] != -1 and rgn[i] != -1:
        ans += 1

print(ans)
"""
오큰수, 좌큰수를 구할 수 있다고 가정
임의의 k 에 대하여 k 가 최대값을 가지면서 조건을 만족하는 경우는 한 가지밖에 없다.
-> 


"""

