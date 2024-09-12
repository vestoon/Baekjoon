import sys
input = sys.stdin.readline
TS = int(input())
INF = sys.maxsize


def bellman_ford(src):
    distance = [INF for x in range(N + 1)]
    distance[src] = 0

    for v_num in range(N):
        for S, E, T in edges:
            if distance[S] + T < distance[E]:
                distance[E] = distance[S] + T
                if v_num == N - 1:
                    return False

    return True


# 도로는 방향이 없지만 웜홀은 방향이 있다
for _ in range(TS):
    # N: 정점의 개수, M: 도로의 개수, W: 웜홀의 개수
    N, M, W = map(int, input().split())
    edges = []  # (S, E, T)
    # 초기화
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    if bellman_ford(1):
        print("NO")
    else:
        print("YES")