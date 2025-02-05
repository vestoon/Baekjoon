import sys
sys.setrecursionlimit(210000)
input = sys.stdin.readline

N = int(input())
adj_list = [[] for x in range(N+1)]
parent = [0 for x in range(N+1)]
time_b = [N+1 for x in range(N+1)] # a 가 이 노드에 도달하는 시간
time_c = [N+1 for x in range(N+1)] # b 가 이 노드에 도달하는 시간

for _ in range(N-1):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

a, b, c = map(int, input().split()) # 윤이(도둑) 달구, 포닉스

# parent 초기화
def make_tree(cur, prev):

    for nxt in adj_list[cur]:
        if nxt == prev: continue

        parent[nxt] = cur
        make_tree(nxt, cur)
make_tree(a, 0)

# time_b, time_c 만들기
t = 0
while b != a:
    time_b[b] = t
    t += 1
    b = parent[b]
t = 0
while c != a:
    time_c[c] = t
    t += 1
    c = parent[c]

def escape(cur, t):
    if time_b[cur] <= t or time_c[cur] <= t: # 경찰이랑 만나는 경우
        return False
    
    if len(adj_list[cur]) == 1:
        return True

    for nxt in adj_list[cur]:
        if nxt == parent[cur] : continue

        if time_b[nxt] == N+1 and time_c[nxt] == N+1:
            return True

        if escape(nxt, t+1):
            return True
    
    return False

print("YES" if escape(a, 0) else "NO")

"""
윤이가 있는 노드를 루트 노드로 지정
인접 리스트하고 parent 리스트 만들기
후 두 경찰이 위로 올라가면서 각 노드에 도달하는 시간 기록

윤이가 아래로 dfs로 내려가면서 리프에 도달하면 종료
경찰이 먼저 도착하는 곳으로는 갈 수 없다.
"""