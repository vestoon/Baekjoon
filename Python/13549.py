import collections
N, K = map(int, input().split())

visited = [False for x in range(100001)]
q = collections.deque()
while N <= 100000:
    visited[N] = True
    q.append(N)
    if N == K:
        find = True
        break
    N *= 2


# 곱하기: 배열 순회하면서 최소값 처리
find = False
distance = 0
while q:
    distance += 1
    if find:
        break
    print(q)
    l = len(q)
    for _ in range(l):
        x = q.popleft()
        if x != 0 and not visited[x-1]:
            if x-1 == K:
                find = True
                break
            q.append(x-1)
            visited[x-1] = True
        if x != 100000 and not visited[x+1]:
            if x+1 == K:
                find = True
                break
            q.append(x+1)
            visited[x+1] = True
    if find:
        break

    print(q)
    l = len(q)
    for _ in range(l):
        x = q.popleft()
        q.append(x)
        x *= 2
        while x <= 100000 and not visited[x]:
            q.append(x)
            visited[x] = True
            if x == K:
                find = True
                break
            x *= 2
        if find:
            break

    if find:
        break
print(distance)



