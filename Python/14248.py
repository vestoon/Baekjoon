import sys
sys.setrecursionlimit(110000)
input = sys.stdin.readline

n = int(input())
nxt = list(map(int, input().split()))
visited = [False for x in range(n)]
s = int(input())-1

cnt = 0 # 도달할 수 있는 정점의 수

def dfs(cur):
    global cnt
    cnt += 1
    visited[cur] = True

    if cur + nxt[cur] < n and not visited[cur+nxt[cur]]:
        dfs(cur+nxt[cur])
    
    if 0 <= cur - nxt[cur] and not visited[cur-nxt[cur]]:
        dfs(cur-nxt[cur])

dfs(s)
print(cnt)
