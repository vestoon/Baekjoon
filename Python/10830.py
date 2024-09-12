N, B = map(int, input().split())
A = []
for _ in range(N):
    line = list(map(int, input().split()))
    for i in range(N):
        line[i] %= 1000
    A.append(line)


def mat_mul(a, b):
    ret = [[0 for x in range(len(b[0]))] for y in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            tmp = 0
            for k in range(len(b)):
                tmp += (a[i][k]*b[k][j]) % 1000
            ret[i][j] = tmp % 1000

    return ret


def cal(m, n):  # pow
    # print(n)
    if n == 1:
        return m
    if n == 2:
        return mat_mul(m, m)

    sub = cal(m, n//2)
    if n % 2:
        return mat_mul(mat_mul(sub, sub), m)

    return mat_mul(sub, sub)


ans = cal(A, B)

for x in ans:
    print(*x)
