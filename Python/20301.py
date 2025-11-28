import sys
from collections import deque
input = sys.stdin.readline

N, K, M = map(int, input().split())

"""
N 명의 사람들 중 K 번째 사람들을 계속 제거해 나가는데 m번째 마다 방향을 바꾼다
"""

que = deque([str(x) for x in range(1, N+1)])	
direction = 1
d_cnt = 0 # 제거된 사람 수 % M
ans = []

while que:
	if direction == 1:
		que.rotate(-(K-1))
		ans.append(que.popleft())
	else:
		que.rotate(K-1)
		ans.append(que.pop())

	d_cnt += 1
	if d_cnt == M:
		direction *= -1
		d_cnt = 0

sys.stdout.write("\n".join(ans))