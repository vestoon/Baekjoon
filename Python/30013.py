import sys
input = sys.stdin.readline

N = int(input())
record = list(input().rstrip())
"""
측정 기록 상 가능한 가장 적은 귀뚜라미 수를 구하기

모든 주기의 경우의 수에 대해서 완탐, 탐색 시간은 N^2

"""
ans = N

# l 주기
for l in range(1, N+1):
    cnt = 0

    for i in range(N):
        if record[i] == '.': continue
        if i - l < 0:
            cnt += 1
        elif record[i-l] == '.': # 바로 이전 울음소리만 확인해도 새로운 구간인지 아닌지 알 수 있다.
            cnt += 1

    ans = min(ans, cnt)

print(ans)         
