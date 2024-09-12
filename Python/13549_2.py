import collections

N, K = map(int, input().split())

visited = [False for x in range(100001)]
find = False
time = 0

dq = collections.deque()
dq.append(N)
visited[N] = True
N *= 2

while N <= K and N:
    dq.append(N)
    visited[N] = True
    N *= 2
if N <= 100000 and not visited[N]:
    dq.append(N)
    visited[N] = True

while dq:
    l = len(dq)
    # print(dq)
    for _ in range(l):
        front = dq.popleft()
        if front == K:
            find = True
            break

        if front != 0 and not visited[front-1]:
            dq.append(front-1)
            visited[front-1] = True
        if front < K and not visited[front+1]:
            dq.append(front+1)
            visited[front+1] = True

    if find:
        break
    time += 1
    l = len(dq)
    # print(dq)
    for _ in range(l):
        front = dq.popleft()
        if front == K:
            find = True
            break

        dq.append(front)
        front *= 2
        while front <= K and front:
            if not visited[front]:
                dq.append(front)
                visited[front] = True
            front *= 2
        if front <= 10000 and not visited[front]:
            dq.append(front)
            visited[front] = True
    if find:
        break

print(time)
