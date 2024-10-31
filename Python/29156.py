import sys
import math
input = sys.stdin.readline
N = int(input())

idx = [] # 각 탭들의 중앙의 좌표
end = 0 # 마지막으로 입력받은 탭의 가장 오른쪽 좌표
for _ in range(N):
    l = int(input())
    idx.append(end+l/2)
    end += l
L = int(input())
Q = int(input())

for _ in range(Q):
    x = int(input()) # 사용자가 클릭한 탭의 번호, 1부터 센다
    x -= 1

    if idx[x] <= L/2 or end < L: # 중앙보다 왼쪽에 있을 때 혹은 그냥 길이가 짧을 때 
        # print(math.floor(idx[x]*100)/100)
        print("0.00")
        continue

    d = min(idx[x] - L/2, end - L)
    
    print(f"{math.floor((d)*100)/100:.2f}") 


