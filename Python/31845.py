import sys
import collections
input = sys.stdin.readline

"""
제일 높은 카드부터 가져가야 하고 음수인 카드는 버려야 한다
남은 카드가 음수밖에 없다면 조커 가져오기 -> 이후 음수인 페어를 버려야 하나?
문제는 양수를 다 가져올 수 없다는거
"""

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

que = collections.deque(arr)

joker = False  # 플레이어에게 있을 때 True
score = 0
while M and que:
    M -= 1

    pickMax = que.pop()
    if pickMax <= 0 and not joker:
        joker = False
    else:
        score += pickMax
    
    # 내 꺼 버리기
    if joker:
        joker = False
    elif que:
        que.popleft()
    else:
        break

print(score)