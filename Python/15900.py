import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
adj_list = [[] for x in range(N+1)]
total_cnt = 0

for _ in range(N-1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


def dfs(cur, d, prev):
    # 리프 노드에 도달한 경우
    if len(adj_list[cur]) == 1  and  cur != 1:
        return d
    
    ret = 0
    for nxt in adj_list[cur]:
        if nxt == prev: continue
        ret += dfs(nxt, d+1, cur)

    return ret

total_cnt = dfs(1, 0, -1)
print("Yes" if total_cnt%2 else "No")