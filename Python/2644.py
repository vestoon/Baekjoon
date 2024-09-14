import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
adj_list = [[] for x in range(n+1)]


for _ in range(m):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)


def dfs(prev, cur, dst):

    for nxt in adj_list[cur]:
        if nxt == prev:
            continue
        if nxt == dst:
            return 1
        
        d = dfs(cur, nxt, dst)
        if d:
            return d+1
    
    return 0


def dfs2(prev, cur, dst, acc):
    if cur == dst:
        print(acc)
        return True

    for nxt in adj_list[cur]:
        if nxt == prev: continue

        if dfs2(cur, nxt, dst, acc+1):
            return True
    
    return False

    


# ans = dfs(0, a, b)
# print(ans if ans else -1)

if not dfs2(0, a, b, 0):
    print(-1)