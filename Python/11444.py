N = int(input())
k = N//2
mod = 1000000007

A = [[1, 1],
     [1, 2]]


def mat_mul(x, y):
    # ret = [[x[0][0]*y[0][0]%mod + x[0][1]*y[1][0]%mod, x[0][0]*y[0][1]%mod + x[0][1]*y[1][1]%mod],
    #        [x[1][0]*y[0][0]%mod + x[1][1]*y[1][0]%mod, x[1][0]*y[0][1]%mod + x[1][1]*y[1][1]%mod]]
    ret = [[(x[0][0] * y[0][0] + x[0][1] * y[1][0]) % mod, (x[0][0] * y[0][1]  + x[0][1] * y[1][1]) % mod],
           [(x[1][0] * y[0][0] + x[1][1] * y[1][0])% mod, (x[1][0] * y[0][1] + x[1][1] * y[1][1]) % mod]]
    return ret


# A 의 x승 계산
def mat_pow(x):
    if x == 1:
        return A
    B = mat_pow(x//2)
    ret = mat_mul(B, B)
    if x % 2:
        return mat_mul(ret, A)
    return ret


if N == 1:
    print(1)
    exit()

ans = mat_pow(k)
if N%2:
    print(ans[1][1])
else:
    print(ans[0][1])