import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = 0 # 노드의 개수
path = list(map(int, input().split()))
visited = [False for x in range(N)]
parent = [-1 for x in range(N)]
st = deque([-1])
for cur in path:
  if visited[cur]:
    st.popleft() # 어차피 한 칸 위로밖에 가지 않음
    continue

  visited[cur] = True
  K = max(K, cur+1)
  parent[cur] = st[0]
  st.appendleft(cur)
  
print(K)
print(*parent[:K])