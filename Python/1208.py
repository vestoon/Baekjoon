import sys
import bisect
input = sys.stdin.readline

"""
중간에서 만나기란?
전체 배열에서 수행했을 때는 2**n이 걸리는 연산을 수열을 절반씩 나누는 방법
좌, 우 배열에서 완탐을 수행해서 2**(n-1)가지 경우의 수를 모두 만들어 논다.

왼쪽 배열의 각 원소에 대해서 매칭되는 값을 오른쪽에서 이분탐색으로 찾아내는 것
시간 복

굳이 나머지 반쪽에서 원하는 값 찾을 때 이분 탐색을 써야 하나? 일단 리스트에 저장해보자
길이 8백만은 필요하다

길이가 0인 부분수열은 그냥 예외처리 하자. 마지막에 S가 0일 경우 정답에서 1을 빼는 식으로
"""

N, S = map(int, input().split())
arr = list(map(int, input().split()))

cases_left = []
cases_right = []
mid = N//2
ans = 0 if S else -1

# recur_left(0, 0)
def recur_left(i:int ,acc:int):
    if i == mid:
        cases_left.append(acc)
        return
    
    recur_left(i+1, acc)
    recur_left(i+1, acc+arr[i])


# recur_right(mid, 0)
def recur_right(i: int, acc:int):
    if i == N:
        cases_right.append(acc)
        return
    
    recur_right(i+1, acc)
    recur_right(i+1, acc+arr[i])


recur_left(0, 0)
recur_right(mid, 0)
cases_right.sort()
# print(cases_left)
# print(cases_right)

for x in cases_left:
    l, r = bisect.bisect_left(cases_right, S-x), bisect.bisect_right(cases_right, S-x)
    # print(l, r)
    ans += r - l

print(ans)


    