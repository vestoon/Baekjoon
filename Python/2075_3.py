import sys
input = sys.stdin.readline

# merge sort 를 이용해보자
def merge(arr1, arr2): # 길이가 N 인 배열 2개를 받아서 길이가 N으로 또 짤라야 함
    i, j = 0, 0
    ans = []
    for _ in range(N):
        a ,b = arr1[i], arr2[j]
        if a < b:
            ans.append(b)
            j += 1
        else:
            ans.append(a)
            i += 1
    return ans

N = int(input())
cur = list(map(int, input().split()))
cur.sort(reverse=True)
for _ in range(N-1):
    nxt = list(map(int, input().split()))
    nxt.sort(reverse=True)
    cur = merge(cur, nxt)
    # print(cur)

print(cur[-1])
# 함수를 만들어써서 그런가 그냥 깡구현보다 시간 더걸림ㅠㅠ
# 메모리가 조큼 더 적다ㅎㅎ
