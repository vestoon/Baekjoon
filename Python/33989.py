N = int(input())
S = input().strip()
"""
결국엔 특정 위치를 기준으로 왼쪽이 전부 B, 오른쪽이 전부 D가 돼야 함
각 위치에서 왼쪽에 D, 오른쪽에 B가 몇 개 있는지 누적 합을 통해서 계산
이후 모든 위치에 대해서 완탐으로 갱신
"""
ans = 1000000

cnt_D = [0 for x in range(N)] # S[:i+1](왼쪽)에 있는 단풍의 개수
cnt_D[0] = 1 if S[0] == 'D' else 0
for i in range(1, N):
  cnt_D[i] = cnt_D[i-1] + 1 if S[i] == 'D' else cnt_D[i-1]

cnt_B = [0 for x in range(N)] # S[i:](오른쪽)에 있는 벚꽃의 개수
cnt_B[-1] = 1 if S[-1] == 'B' else 0
for i in range(N-2, -1, -1):
  cnt_B[i] = cnt_B[i+1] + 1 if S[i] == 'B' else cnt_B[i+1]

# i번째에 가장 왼쪽의 D가 온다고 가정
for i in range(N):
  tmp = cnt_D[i] + cnt_B[i] if S[i] == 'B' else cnt_D[i] + cnt_B[i] - 1
  ans = min(ans, tmp)

# D가 없는 경우도 고려
print(min(ans, cnt_D[-1]))