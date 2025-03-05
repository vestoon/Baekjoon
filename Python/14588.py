import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline
"""
L, R 을 기반으로 인접 행렬을 만들어서 플로이드 와샬 사용
N^2 순회 하면서 두 선분이 겹치는지 확인하고 거리를 초기화
두 선분이 겹치는지 확인하는 공식 : max(a1, a2) <= min(b1, b2)

생각해볼 점)
1. 양방향 리스트인데 인접 행렬을 절반만 쓰면안되는가? 
A : NO! 사실 가능은 하지만 좀 번거롭기 때문에 굳이 싶다.

예시를 들어 2에서 3으로 가는 경로를 찾는데 최단 경로가
2 -> 4 -> 1 -> 3 이라고 해 보자

k=1 일 때 adj_mat[3][4] 는 갱신해 주지만
adj_mat[4][3] 은 갱신하지 않고 k=4 일 때도 2 -> 4 -> 3 은 고려하지 않는다.
이를 해결하려면 

애초에 반복을 돌릴 때 
adj_mat[i][j] = min(adj_mat[i][j], adj_mat[i][k]+adj_mat[k][j])
에서 k와i, k와j 의 대소 관계를 비교해 min안에 들어가는 값을 바꿔줘야 한다. 

그런데 그 귀찮을 걸 제가 해냈습니다! 
adj_mat_ik = adj_mat[i][k] if i < k else adj_mat[k][i]
adj_mat_kj = adj_mat[k][j] if k < j else adj_mat[j][k]
adj_mat[i][j] = min(adj_mat[i][j], adj_mat_ik+adj_mat_kj)

이렇게 바꾸면 시간 조금이나마 줄어듬 2.9 초에서 2초 정도?
"""
def sol():
    N = int(input()) # 선분의 개수
    adj_mat = [[301 for y in range(N+1)] for x in range(N+1)] # 인접 행렬
    for i in range(1, N+1): # 대각성분 초기화
        adj_mat[i][i] = 0 
    lines = [[]]
    
    for fri_num in range(1, N+1):
        L, R = map(int, input().split())
        lines.append((L, R))

    for i in range(1, N+1):
        for j in range(i+1, N+1):
            # i, j 번 친구가 서로 인접해 있는지 검사 후 추가
            A, B = lines[i], lines[j]
            a1, b1 = A
            a2, b2 = B

            # 두 선이 겹치는 경우의 조건식
            if max(a1, a2) <= min(b1, b2):
                # 둘 중 오른쪽에 있는 선분의 a 값이 왼쪽에 있는 선분의 b값보다 같거나 작아야 함
                adj_mat[i][j] = 1

    # 플로이드 와샬 (i < j)
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(i+1, N+1):
                adj_mat_ik = adj_mat[i][k] if i < k else adj_mat[k][i]
                adj_mat_kj = adj_mat[k][j] if k < j else adj_mat[j][k]
                adj_mat[i][j] = min(adj_mat[i][j], adj_mat_ik+adj_mat_kj)

    # 쿼리 처리
    Q = int(input())
    for _ in range(Q):
        A, B = map(int, input().split())
        ans = adj_mat[A][B] if A < B else adj_mat[B][A] # 대소 관계 유지
        print(ans if ans != 301 else -1)
    

sol()