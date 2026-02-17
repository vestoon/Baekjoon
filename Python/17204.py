import sys
input = sys.stdin.readline

N, K = map(int, input().split())
pointer = [-1 for x in range(N)]
visited = [False for x in range(N)]

for i in range(N):
  a = int(input())
  pointer[i] = a

cur = 0
cnt = 0
while cur != K and not visited[cur]:
  visited[cur] = True
  cnt += 1
  cur = pointer[cur]

print(cnt if cur == K else -1)
