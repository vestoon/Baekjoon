import sys
import collections
sys.setrecursionlimit(10000)
input = sys.stdin.readline

V, E = map(int, input().split())
adj_list = [[] for x in range(V+1)]
adj_listT = [[] for x in range(V+1)]
visited = [False for x in range(V+1)]
st = collections.deque()
ans = []

def dfs(cur):
    visited[cur] = True
    for nxt in adj_list[cur]:
        if not visited[nxt]:
            dfs(nxt)
    
    st.append(cur)

def dfsT(cur, scc):
    visited[cur] = True

    for nxt in adj_listT[cur]:
        if not visited[nxt]:
            scc += dfsT(nxt, [nxt])

    return scc

for _ in range(E):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_listT[v].append(u)

for cur in range(1, V+1):
    if not visited[cur]:
        dfs(cur)
visited = [False for x in range(V+1)]

while st:
    cur = st.pop()
    if visited[cur]:
        continue
    scc = dfsT(cur, [cur])
    scc.sort()
    ans.append(scc)

ans.sort()
print(len(ans))
for scc in ans:
    print( *scc, -1)

# print(ans)
