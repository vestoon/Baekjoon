from collections import deque
N = int(input())

que = deque([x for x in range(1, N+1)])
while que:
    print(que.popleft(), end=' ')

    if que:
        que.append(que.popleft())
    