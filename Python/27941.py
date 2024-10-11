import sys
from collections import defaultdict

cor = [defaultdict(int) for x in range(11)]
for _ in range(2047):
    vertex = list(map(int, input().split()))
    for i in range(11):
        cor[i][vertex[i]] += 1

for i in range(11):
    for v in cor[i]:
        if cor[i][v] == 1023:
            print(v, end=' ')