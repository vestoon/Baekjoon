import sys
import math
input = sys.stdin.readline

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

N = int(input()) # 1 ~ 1000
signals = {} # x : [y1, y2, ...]
for i in range(N):
    x, y = map(int, input().split())
    if x in signals:
        signals[x][0] = min(signals[x][0], y)
        signals[x][1] = max(signals[x][1], y)
    else:
        signals[x] = [y, y]

keys = sorted(list(signals.keys()))
prevX = keys[0]
dp = [(0, y) for y in signals[keys[0]]] # 현재지 마지막 신호의 y 좌표, 누적된 거리

for curX in keys[1:]:
    # print(prevX, curX)
    tmp = []

    for curY in signals[curX]:
        curAcc = 0 # 현재 x 좌표에서 curY를 선택했을 때의 최대 시스템 길이
        for acc, prevY in dp:
            curAcc = max(curAcc, acc + dist(prevX, prevY, curX, curY))
        
        tmp.append((curAcc, curY))

    dp = tmp
    prevX = curX

print(max(dp)[0])
# print(dp)

"""
같은 x 좌표를 가지는 신호 중에서 어떤 값을 선택하는게 최선인지를 맞추는 문제

아마도 dp? 

"""

