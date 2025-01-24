import sys
input = sys.stdin.readline

N, T = map(int, input().split())
nxts = [0] + list(map(int, input().split()))
order = [0 for x in range(N+1)]
order[1] = 1

"""
사이클이 무조건 시작 지점으로 돌아온다는 보장이 없다. 

중간 지점이라도 사이클을 찾으려면 일단 방문 처리 배열이 있어야 하고.
방문 처리된 지점을 만났을 때에 길이를 구하기 쉬웠으면 좋겠는데
각 노드에 방문 순서를 저장하도록 할까?

dfs 수행하면서 사이클 찾기 -> 정점당 간선이 하나라서 dfs가 아니어도 될지도?

"""

rest = T # 남은 탐색 횃수
cur = 1 # 현재 탐색 중인 정점
path = [] # 탐색 순서

while rest:
    path.append(cur) # 경로에 cur 추가
    nxt = nxts[cur]

    # 사이클 발생생
    if order[nxt]:
        # ex : 1 2 3 4 5 6 3
        order_cycle_src = order[nxt] # 사이클의 시작점의 방분 순서
        order_cycle_dst = order[cur] # 사이클의 마지막 부분의 방분 순서
        cycle_len = order[cur] - order[nxt] + 1 # 반복되는 구간의 길이
        base = order_cycle_src-1 # 앞쪽 반복되지 않는 부분의 길이이
        r = (T-base) % cycle_len + 1 # 사이클 내부에서 반복되고 멈춘 부분에서의 길이

        cur = path[base + r - 1]
        break

    
    order[nxt] = order[cur] + 1 # order 갱신
    cur = nxt # cur 변경
    rest -= 1 # rest 감소

print(cur)


