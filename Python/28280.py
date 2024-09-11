import sys
import collections
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    find = False
    k = int(input())
    cnt = 0

    q = collections.deque()
    q.append(1)
    visited = [False for x in range(2*k+1)]
    visited[1] = True

    while q:
        l = len(q)

        for _ in range(l):
            cur = q.popleft()
            # print('cur', cur)

            if cur == k:
                find = True
                break

            if cur < k and not visited[cur*2]:
                visited[cur*2] = True
                q.append(cur*2)
            if 1 < cur and not visited[cur-1]:
                visited[cur-1] = True
                q.append(cur-1)

        if find:
            break
        cnt += 1

    print(cnt)

