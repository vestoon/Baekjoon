import collections

N, K = map(int, input().split())

visited = [False for x in range(100001)]
cases_list = [0 for x in range(100001)]
visited[N] = True
cases_list[N] = 1
q = collections.deque()
q.append((N, 1))
time = -1
find = False

while not find:
    l = len(q)
    visit_list = []
    for _ in range(l):
        front, case = q.popleft()
        if front == K:
            find = True
            continue

        if front < 100000 and not visited[front+1]:
            visit_list.append(front+1)
            cases_list[front+1] += case
        if 0 < front and not visited[front-1]:
            visit_list.append(front-1)
            cases_list[front-1] += case
        if front*2 <= 100000 and not visited[front*2]:
            visit_list.append(front*2)
            cases_list[front*2] += case

    for v in visit_list:
        if not visited[v]:
            visited[v] = True
            q.append((v, cases_list[v]))

    time += 1

print(time)
print(cases_list[K])

