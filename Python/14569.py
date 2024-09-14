import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
# 시간표에 과목들 id 를 때려 박는다
# 학생마다 시간대를 돌면서 id 의 개수를 확인한다.
# id 개수가 부족하지 않은 과목의 수만 샌다.


timeTable = [[] for x in range(51)] # 
subCnt = [0 for x in range(N)] # i 번째 과목의 총 몇 개의 칸을 차지하는지

for subId in range(N):
    inp = list(map(int, input().split()))
    subCnt[subId] = inp[0]
    for t in inp[1:]:
        timeTable[t].append(subId)

M = int(input())
for _ in range(M):
    inp = list(map(int, input().split()))
    candidate = defaultdict(int)
    for t in inp[1:]:
        for sub in timeTable[t]:
            candidate[sub] += 1
    
    cnt = 0
    for sub in candidate:
        if candidate[sub] == subCnt[sub]:
            cnt += 1
    
    print(cnt)