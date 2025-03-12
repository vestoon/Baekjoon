import collections
N, K = map(int, input().split())
que = collections.deque([x for x in range(1, N+1)])

print('<', end='')
while que:
    for _ in range(K-1):
        que.append(que.popleft())
    print(que.popleft(), end='')
    if que:
        print(', ', end='')
print('>')