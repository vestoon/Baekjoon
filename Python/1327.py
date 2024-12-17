import collections

N, K = map(int, input().split())
arr = input().split()

"""
8! = 40,320 (4만)
"""

# inp로 들어온 문자열을 i 부터 i+k 까지 스왑한 문자열을 리턴
def swap(inp, i, k): 
    ret = inp[:i]
    for j in range(i+k-1, i-1, -1):
        ret += inp[j]
    ret += inp[i+k:]
    return ret

src = ''
for x in range(1, N+1):
    src += str(x)
target = ''.join(arr)

def bfs(src, target):
    que = collections.deque()
    visited = {src: 0}
    
    que.append(src)
    while que:
        cur = que.popleft()
        if cur == target:
            return visited[target]

        for i in range(N-K+1):
            nxt = swap(cur, i, K)
            if nxt not in visited:
                visited[nxt] = visited[cur]+1
                que.append(nxt)

    return -1

print(bfs(src, target))

    