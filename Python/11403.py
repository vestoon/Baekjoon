import sys
import collections
N = int(sys.stdin.readline())
ad_list = []  # i 행 j 열 ,   i에서 j 로 가는 경로가 있으면 1

#인접 행렬 구축
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    ad_list.append(line)


# print(ad_list)
for i in range(N):
    for j in range(N):
        # 여기서 i 에서 j 로 가는 경로를 탐색
        visited = [False for x in range(N)]
        q = collections.deque()
        q.append(i)
        while q:
            front = q.popleft()
            nxts = [x for x in range(N) if ad_list[front][x]]
            for nxt in nxts:
                if nxt == j:
                    print(1, end=' ')
                    break
                elif not visited[nxt]:
                    q.append(nxt)
                    visited[nxt] = True
            else:
                continue
            break
        else:
            print(0, end=' ')
    print()
