import sys
input = sys.stdin.readline

T = int(input()) 
for scenario in range(1, T+1):
  S, F = map(int, input().split()) # 목표 스탬프 수, 친구 수
  stamps = list(map(int, input().split()))
  stamps.sort(reverse=True)

  cnt_stamps = 0
  cnt_friends = 0
  for stamp in stamps:
    cnt_stamps += stamp
    cnt_friends += 1

    if S <= cnt_stamps:
      break
  else:
    cnt_friends = -1
  
  print(f"Scenario #{scenario}:")
  print(cnt_friends if cnt_friends != -1 else "impossible")
  print()