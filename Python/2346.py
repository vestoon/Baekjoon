import sys
from collections import deque

N = int(input())
nxts = list(map(int, input().split()))

# <1, 2, 3, 4, 5>
que = deque([(i+1, nxts[i]) for i in range(N)])

while que:
    cur, nxt = que.popleft()
    print(cur, end=' ')

    if not que:
        break
    if nxt < 0: # 왼쪽으로 움직인다
        nxt *= -1
        for _ in range(nxt):
            que.appendleft(que.pop())
    else: # 0 < nxt : 오른쪽으로
        for _ in range(nxt-1): # 이미 cur을 pop 한 상태이기 때문에 한번 덜 움직인다.
            que.append(que.popleft())
