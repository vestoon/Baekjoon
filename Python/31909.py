import sys
input = sys.stdin.readline

N = int(input())
cmds = list(map(int, input().split()))
K = int(input())

# P[x] : Px번에 위치한 키의 번호
P = [x for x in range(8)]
exp2 = [2**i for i in range(8)]

def find_ij(cmd):
    for i in range(8):
        for j in range(8):
            if exp2[i] + exp2[j] == cmd:
                P[i], P[j] = P[j], P[i]
                return


for cmd in cmds:
    find_ij(cmd)


print(P[K])
