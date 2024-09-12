import sys
TS = int(sys.stdin.readline())




# 도로는 방향이 없지만 웜홀은 방향이 있다
for _ in range(TS):
    # N: 정점의 개수, M: 도로의 개수, W: 웜홀의 개수
    N, M, W = map(int, sys.stdin.readline().split())
    adjMat = [[0 for x in range(N+1)] for y in range(N+1)]

    # 자신으로 돌아오는 cycle 중에 가장 시간이 적게 걸리는걸 리턴하게 해야 하나?
    # 매개변수가 돌아와야 하는 지점, 중간 지점, 누적 시간 총 세개?
    # dfs 를 이용한 사이클 완전탐색, 방문한 적 있는 정점을 발견하면 사이클 기록하고 바로 다음 반복을 수행
    visited = [False for x in range(N+1)]
    flag = False
    cycle = []
    def dfs(cur, acc):
        visited[cur] = True

        for nxt in range(1, N+1):
            if (not adjMat[cur][nxt]) or (nxt == cur):
                continue
            if not visited[nxt]:
                dfs(nxt, cur + adjMat[nxt])


        visited[cur] = False

    # 초기화
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        adjMat[S][E] = T
        adjMat[E][S] = T
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        adjMat[S][E] = -1*T

