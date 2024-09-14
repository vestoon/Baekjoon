import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
NGE = [0 for x in range(N)]           
st = deque()

for i in range(N-1, -1, -1):

    while st:
        cmp = st.popleft()  # 스택에서 값 가져옴

        if arr[i] < cmp: # 현재 값보다 크다면 오큰수
            st.appendleft(cmp) # 다시 쓸 수도 있기 때문에 다시 넣어줘야 함
            st.appendleft(arr[i]) # 지금 값도 넣어줌
            NGE[i] = cmp
            break
    else:
        # 스택을 다 뽑아도 오큰수를 찾지 못한 경우
        NGE[i] = -1  # -1 입력
        st.appendleft(arr[i]) # 스택에 그 값 저장


print(*NGE)


# 오른쪽에 있는 수 중 자기보다 크면서 가장 가까운거
    
