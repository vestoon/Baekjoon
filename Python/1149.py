import sys
N = int(sys.stdin.readline())
RGB = [[], [], []]
for _ in range(N):
    r, g, b = map(int, sys.stdin.readline().split())
    RGB[0].append(r)
    RGB[1].append(g)
    RGB[2].append(b)

possibility = ((1, 2), (2, 3), (1, 3))
line0 = [(0, 0) for _ in range(N)]  # (acc, RGB)
line1 = [(0, 0) for _ in range(N)]
line2 = [(0, 0) for _ in range(N)]


def dp(n):
    # 3에서 빼는 식으로 나머지 RGB를 계산하자
    rgb0 = 3-line0[n-1][1]-line1[n-1][1]
    rgb1 = 3-line1[n-1][1]-line2[n-1][1]
    rgb2 = 3-line0[n-1][1]-line2[n-1][1]
    line0[n] = (min(line0[n-1][0], line1[n-1][0]) + RGB[rgb0][n], rgb0)
    line1[n] = (min(line1[n-1][0], line2[n-1][0]) + RGB[rgb1][n], rgb1)
    line2[n] = (min(line0[n-1][0], line2[n-1][0]) + RGB[rgb2][n], rgb2)


#RGB 중 무었을 선택한건지 인덱스를 가지고 있어야 한다
# RGB 순으로 012
line0[0] = (RGB[0][0], 0)  # 01
line1[0] = (RGB[1][0], 1)  # 12
line2[0] = (RGB[2][0], 2)  # 02

for i in range(1, N):
    dp(i)

# print(line0)
# print(line1)
# print(line2)
print(min(line0[-1][0], line1[-1][0], line2[-1][0]))
