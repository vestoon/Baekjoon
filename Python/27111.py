import sys
input = sys.stdin.readline

N = int(input())
cnt = 0 # 지금 부대 안에 있다고 상정하는 인원의 수
miss = 0 # 놓친 기록의 수

visited = [False for x in range(200001)]
for _ in range(N):
    a, b = map(int, input().split())

    if b: # 들어오는 기록
        if visited[a]:# 이미 들어와 있는 경우 누락된 기록 1 증가
            miss += 1
        else:
            visited[a] = True
            cnt += 1
    
    else: # 나가는 기록일 경우
        if visited[a]:
            visited[a] = False
            cnt -= 1
        else:
            miss += 1

print(cnt + miss)



