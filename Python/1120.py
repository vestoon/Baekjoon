import sys
input = sys.stdin.readline

A, B = input().split()

"""
B에서 A와 가장 일치하는 부분을 찾는 문제
그냥 완탐 돌려도 복잡도 안걸릴 것 같은데?
"""

ans = len(B) # 구하고자 하는 문자열 차이의 최소값

for i in range(len(B)-len(A)+1):
    cnt = 0 # 틀린 문자열의 개수

    for j in range(len(A)):
        if B[i+j] != A[j]:
            cnt += 1
    ans = min(ans, cnt)

print(ans)