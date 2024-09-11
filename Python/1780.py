import sys
N = int(input())
paperI = []  # 인풋으로 받은 paper
for g in range(N):
    paperI.append(list(map(int, sys.stdin.readline().split())))


# 012 345 678
# 0 ~ k, k ~ 2k, 2k ~ 3k

# [row[:] for row in paper[:] ]

def sol(paperF):  # p: paper
    score = {x: 0 for x in range(-1, 2)}

    def rec(paperR):
        length = len(paperR)
        k = int(length/3)
        ab = paperR[0][0]
        for i in range(length):
            for j in range(length):
                if paperR[i][j] == ab:
                    continue
                else:
                    break
            else:  # 전부 통과한 경우
                continue
            break
        else:
            score[ab] += 1
            return
        idx = [(0, k), (k, 2 * k), (2 * k, 3 * k)]
        for row in idx:
            for col in idx:
                rec([r[col[0]:col[1]] for r in paperR[row[0]:row[1]]])
        return

    rec(paperF)
    for s in range(-1, 2):
        print(score[s])


sol(paperI)

