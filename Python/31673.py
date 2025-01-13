import sys
input = sys.stdin.readline

# N: 학생단체 수, M: 총 예산
N, M = map(int, input().split())

# 각 학생 단체가 가진 표의  수
votes = list(map(int, input().split()))
votes.sort(reverse=True)
total = sum(votes) # 표 절반만 얻어도 탄핵 안당함
target = total//2 # 표의 수가 target을 넘으면 탄핵당함

cnt = 0 # 현재 얻은 표 수
for i in range(N):
    cnt += votes[i]
    if total <= cnt*2:
        break

# i+1개의 단체에만 예산 분배하면 된다 학생회 생각하면 i+2  21

print(M//(i+2))