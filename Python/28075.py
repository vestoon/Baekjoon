N, M = map(int, input().split())
grid = [list(map(int, input().split())) for x in range(2)]
cnt = 0

def search(prev, point, day):
  global cnt
  if day == N:
    if M <= point:
      cnt += 1
    return
  
  for i in range(2):
    for j in range(3):
      if prev == j:
        search(j, point + grid[i][j]//2, day+1)
      else:
        search(j, point + grid[i][j], day+1)

search(-1, 0, 0)
print(cnt)