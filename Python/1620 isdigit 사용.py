import sys

N, M = map(int, sys.stdin.readline().split())


pkm = {}
for i in range(1, N+1):
    pokemon = sys.stdin.readline().rstrip()
    pkm[i] = pokemon
    pkm[pokemon] = i
# print(pkm)

for q in range(M):
    qst = sys.stdin.readline().rstrip()
    # print('Q:', qst)
    if qst.isdigit():
        print(pkm[int(qst)])
    else:
        print(pkm[qst])


    

