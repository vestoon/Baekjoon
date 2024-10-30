import sys
import collections
input = sys.stdin.readline

N = int(input())
workTime = collections.defaultdict(int)
m, M = sys.maxsize, 0

for weekNum in range(N):
    period = [4, 6, 4, 10]
    for partTime in period:
        people = input().split()
        for p in people:
            if p == '-': continue
            workTime[p] += partTime

m = min(workTime.values()) if workTime else 0
M = max(workTime.values()) if workTime else 0
print("No" if M-m > 12 else "Yes")
