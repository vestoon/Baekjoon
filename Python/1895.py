import sys
input = sys.stdin.readline

R, C = map(int, input().split())
image = []
for _ in range(R):
  image.append(list(map(int, input().split())))
T = int(input())

cnt = 0
for i in range(R-2):
  for j in range(C-2):
    vals = []
    for ii in range(i, i+3):
      for jj in range(j, j+3):
        vals.append(image[ii][jj])
    vals.sort()
    if T <= vals[4]:
      cnt += 1

print(cnt)
