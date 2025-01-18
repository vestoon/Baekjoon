import sys
input = sys.stdin.readline

N = int(input())
refs = list(map(int, input().split()))
upper = [0 for x in range(10002)] # x+1번 이상 인용된 논문의 수
lower = [0 for x in range(10002)] # x+1번 이하 인용된 논문의 수
"""
k 미만  |  k  |  k 초과


n-k 편의 눈문들 인용회수가 각각 k번 이하이다
<-> 인용회수가 k 초과인 논문의 수가 k보다 같거나 작다

0 ~ 10,000 까지 모든 인용 횟수에 대해 논문 수를 카운팅 -> 1,000
0 ~ 10,000 인용 횟수 중에서 논문 수가 일치하는 최대값 찾기 
3, 4, 5, 8, 10

k 개의 논문은 k개 이상의 인용을 가지고 있고
나머지 n-k 개의 논문은 k 이하의 인용을 가지고 있도록 해야 한다


1 2 3 4 5 6 7 8 9 10
0 0 1 1 1 0 0 1 0 0
"""

for ref in refs:
    upper[ref] = 1
    lower[ref] = 1
# print(upper[:13])

for i in range(10001):
    lower[i] += lower[i-1]
for i in range(10000, 0, -1):
    upper[i] += upper[i+1]

print(upper[:13])
print(lower[:13])

for k in range(0, 10001):
    if k <= upper[k] and N-k <= lower[k]:
        print(k)
        break
