from collections import deque
A, K = map(int, input().split())

visited = [False for x in range(1000001)]
que = deque()
que.append(A)
cnt = 0
find = False

while que:
    l = len(que)
    for _ in range(l):
        cur = que.popleft()

        if cur == K:
            find = True
            break

        for nxt in [cur+1, cur*2]:
            if K < nxt or visited[nxt]:
                continue
            
            visited[nxt] = True
            que.append(nxt)
    
    if find:
        break
    cnt += 1

print(cnt)