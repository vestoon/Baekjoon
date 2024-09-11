# 딕셔너리를 만들어서 mbti별로 몇 명이 있는지 저장
# 3명 이상이 있으면 그냥 0 출력
# 나머지는 그냥 깡으로 계산해야 할 듯?
import sys
T = int(sys.stdin.readline())


def mind_distance(a, b):
    count = 0
    for i in range(4):
        if a[i] != b[i]:
            count += 1

    return count


def mind_distance_of_trio(a, b, c):
    acc = 0
    acc += mind_distance(a, b) + mind_distance(b, c) + mind_distance(a, c)

    return acc


for _ in range(T):
    N = int(sys.stdin.readline())
    mbtis = sys.stdin.readline().split()
    db = {}
    for mbti in mbtis:
        db[mbti] = db.get(mbti, 0) + 1

    for key in db:
        if db[key] >= 3:
            break
    else:
        m = 12
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    m = min(m, mind_distance_of_trio(mbtis[i], mbtis[j], mbtis[k]))

        print(m)
        continue
    print(0)










