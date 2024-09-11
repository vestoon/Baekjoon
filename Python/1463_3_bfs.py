import collections

N = int(input())


def nxts(n):
    ans = []
    if n > 0:
        ans.append(n-1)
    if not n%2:
        ans.append(n//2)
    if not n%3:
        ans.append(n//3)
    return ans


visited = [False for x in range(N+1)]
visited[N] = True
find = True if N == 1 else False
q = collections.deque()
q.appendleft(N)
time = 0

while q:
    if find:
        break
    time += 1
    l = len(q)
    for _ in range(l):
        front = q.popleft()

        for nxt in nxts(front):
            if nxt == 1:
                find = True
                break

            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True

print(time)
