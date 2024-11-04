import sys
input = sys.stdin.readline

N, K = map(int, input().split())
wines = list(map(int, input().split()))
wines.sort()
ans = 0
last = 0

"""
일단 정렬

계속 오름차순일 순 없다. 그냥 최대값을 박는데 무조건 더 이득이기 때문에 결국엔
내림차순인 부분 수열이 무조건 하나는 생긴다.

언젠가는 내림차순이 하나는 무조건 생긴다고 생각해 보자 그 사이에 무언가 다른 수를 넣는게 
의미가 있을까? -> 사이에 다른 수를 넣는 것은 그냥 공간의 낭비일 뿐이다. 
때문에 오르락내리락을 반복해야 한다. 
"""

for i in range(K):
    if i%2:
        last = wines[i//2]
    else:
        ans += wines[-(i//2 + 1)] - last


print(ans)