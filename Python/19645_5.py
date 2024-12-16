import sys
input = sys.stdin.readline

"""
4번 솔루션에서 좀 더 최적화 해보자
기본적으로 50 * 2500*2500 의 탐색이 너무 오래 걸린다.
total*total 사이즈의 dp 배열을 생성해서 모든 i, j 조합의 경우의 수를 계산
i, j 를 정렬함으로써 상삼각 행렬만 탐색

결과)
pypy 로만 통과하고 python3 로는 통과 불가능
내 선에서 최대한 최적화 한건데 파이썬이 안뚫린다.
"""

N = int(input())
ham = list(map(int, input().split()))
total = sum(ham)

comb = [[False for x in range(total+1)] for y in range(total+1)]
comb[0][0] = True
comb[ham[0]][0] = True
comb[0][ham[0]] = True
best = 0 # 구하고자 하는 막내의 햄버거의 최대값


for n in range(1, N):
    # n 번째 햄버거까지 사용했을 때의 가능한 조합의 수

    for i in range(total, -1, -1):
        for j in range(total, i-1, -1):
            if not comb[i][j]: continue
            comb[i][j] = False

            for ni, nj, nk in [(i+ham[n], j, total-i-ham[n]-j), (i, j+ham[n], total-i-j-ham[n]), (i, j, total-i-j)]:
                # if total < ni or total < nj: continue
                if nj < ni: # ni, nj 정렬
                    ni, nj = nj, ni
                
                comb[ni][nj] = True
                # best = max(best, min(ni, nj, nk))

for i in range(total+1):
    for j in range(i, total+1):
        if not comb[i][j]: continue
        best = max(best, min(i, total-i-j))
        # if best < max(best, min(i, j, total-i-j)):
        #     # print(i, j, max(best, min(i, j, total-i-j)))
        #     best = max(best, min(i, j, total-i-j))

# for i in range(total, -1, -1):
#     for j in range(total, i-1, -1):
#         # k = total-i-j
#         if comb[i][j]:
#             print(i, j)
#             exit()


print(best)