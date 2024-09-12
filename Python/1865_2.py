import sys
TS = int(sys.stdin.readline())

# A에서 B 로 가는 웜홀이 있다고 할 때 다익스트라를 이용해서 B 에서 A 로 가는 path 를 찾아야 하나?
# 이 때는 방문했던 곳을 방문하지 않는다


# 도로는 방향이 없지만 웜홀은 방향이 있다
for _ in range(TS):
    # N: 정점의 개수, M: 도로의 개수, W: 웜홀의 개수
    N, M, W = map(int, sys.stdin.readline().split())
    adjMat = [[0 for x in range(N+1)] for y in range(N+1)]
    wormHoles = []  # (S, E, T)
    # 초기화
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        adjMat[S][E] = T
        adjMat[E][S] = T
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        T *= -1
        adjMat[S][E] = T
        wormHoles.append((S, E, T))


    # 매개변수에 time 를 추가해서 cycle 이 time 을 초과하면 더이상 탐색 안하게 짜보자
    visited = [False for x in range(N+1)]
    def dfs(src, dst):  # src 에서 dst 로 가는 시간 찾기
        if src == dst:
            return 0
        visited[src] = True
        # hasNxt = False
        ret = sys.maxsize

        for nxt in range(1, N+1):
            if visited[nxt] or not adjMat[src][nxt]:
                continue
            # hasNxt = True
            ret = min(ret, dfs(nxt, dst) + adjMat[src][nxt])

        visited[src] = False
        return ret

    for S, E, T in wormHoles:
        # print(dfs(E, S))
        if dfs(E, S) + T < 0:
            print("YES")
            break
    else:
        print("NO")





