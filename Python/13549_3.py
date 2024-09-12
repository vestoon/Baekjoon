# Second version
# Use more memory and less time
# Difference: store the shortest time in visited array
import collections

N, K = map(int, input().split())

visited = [-1 for x in range(100001)]
dq = collections.deque()
dq.append(N)
visited[N] = 0
find = False if visited[K] == -1 else True

while not find:
    front = dq.popleft()
    if front == K:
        break

    if front and front*2 < 100001 and visited[front*2] == -1:
        visited[front*2] = visited[front]
        dq.appendleft(front*2)
    if front != 0 and visited[front-1] == -1:
        visited[front-1] = visited[front] + 1
        dq.append(front-1)
    if front < K and visited[front+1] == -1:
        visited[front+1] = visited[front]+1
        dq.append(front+1)


print(visited[K])
