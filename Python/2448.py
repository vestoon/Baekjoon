N = int(input())
tmp = N//3
k = 0
while not tmp%2:
    tmp //= 2
    k += 1

# 가장 작은 삼각형: 밑변 5, 높이 3
triangle = ["  *  ", " * * ", "*****"]
height = N//3

for _ in range(k):
    tmp = []
    h = len(triangle)
    w = len(triangle[0])
    for line in range(h):
        side = ' '*(w//2+1)
        tmp.append(side + triangle[line] + side)
    for line in range(h):
        tmp.append(triangle[line]+' '+triangle[line])

    triangle = tmp

for line in triangle:
    for x in line:
        print(x, end='')
    print()

