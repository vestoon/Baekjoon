# Second version
# Get less memory and time
# Improvement: find top of fractal and divide into small fractal
# and when you reach the smallest fractal, mark '*'
N = int(input())
pow2K = N//3

ans = [[' ']*(pow2K*6 - 1) for x in range(N)]
offSet = pow2K*3 - 3  # Use math


def print_star(r, c, curN):  # (r, c): left-up coordinate of fractal
    if curN == 3:
        ans[r][c+2] = '*'
        ans[r+1][c+1] = '*'
        ans[r+1][c+3] = '*'
        for x in range(5):
            ans[r+2][c+x] = '*'
    else:
        nxtN = curN//2
        print_star(r, c, nxtN)
        print_star(r+nxtN, c-nxtN, nxtN)
        print_star(r+nxtN, c+nxtN, nxtN)


print_star(0, offSet, N)
for line in ans:
    print(''.join(line))
