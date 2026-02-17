import sys
input = sys.stdin.readline

N, K = map(int, input().split())
pointer = [int(input()) for _ in range(N)]
visited = [False for x in range(N)]

cur = 0
cnt = 0
while cur != K and not visited[cur]:
  visited[cur] = True
  cnt += 1
  cur = pointer[cur]

print(cnt if cur == K else -1)
