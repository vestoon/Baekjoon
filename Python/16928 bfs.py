import sys
import collections

N, M = map(int, sys.stdin.readline().split())  # N: 사다리, M: 뱀
visited = [False for x in range(101)]
board = [x for x in range(101)]
for _ in range(N):
    src, dst = map(int, sys.stdin.readline().split())
    board[src] = dst

for _ in range(M):
    src, dst = map(int, sys.stdin.readline().split())
    board[src] = dst

q = collections.deque()
q.append(1)
count = 0
front = 1
flag = True
while flag:
    for _ in range(len(q)):
        front = q.popleft()
        for dice_num in range(1, 7):
            nxt = front + dice_num
            if nxt <= 100 and not visited[nxt]:
                if board[nxt] == 100:
                    flag = False
                    break
                q.append(board[nxt])
                # print('via:', board[nxt], flag)
                visited[board[nxt]] = True
                visited[nxt] = True
    count += 1
    # print('count', count)

print(count)