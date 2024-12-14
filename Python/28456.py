import sys
input = sys.stdin.readline

N = int(input())
arr2 = [list(map(int, input().split())) for x  in range(N)]
Q = int(input())

for _ in range(Q):
    c, *p = map(int, input().split())

    if c == 1:
        i = p[0] -1 
        arr2[i] = [arr2[i][j-1] for j in range(N)]
    else:
        tmp = [[ arr2[N-1-j][i] for j in range(N)] for i in range(N)]
        arr2 = tmp
        """
        i, j => j, N -i + 1
        arr[i-1][j-1] = tmp[j-1][N-i]
        arr[i][j] = tmp[j][N-i-1]

        arr2[i][j] = tmp[j][N-i-1] I=j , J = N-i-1
        tmp[I][J] = arr2[-J+N-1][I]
        """

for l in arr2:
    print(*l)