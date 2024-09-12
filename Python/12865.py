import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # 100, 200
# used = [False for x in range(N)]
objects = []
for _ in range(N):
    W, V = map(int, input().split())  # 0, 0 으로 예외 발생
    ###
    if W == 0 and V == 0:
        objects = [(1, 1) for x in range(100)]
        break
    ####
    objects.append((W, V))

ans = 0


# objects 의 i 번재에서 i 번째 원소를 가방에 넣었을 때와 안넣었을 때의 2갈래로 나눠서 dfs 수행
def find_max(accV, accW, i):  # i: index of objects
    print(i, end=" ") ###
    if i == N:
        return
    w, v = objects[i]

    # used[cur] = True
    use = False if accW + w > K else True
    global ans

    find_max(accV, accW, i+1)
    if use:
        find_max(accV + v, accW + w, i+1)
        ans = max(ans, accV + v)
    else:
        ans = max(ans, accV)


find_max(0, 0, 0)
print() ###
# print(objects)
print(ans)

# 100 개의 짐을 다 담아도 무게를 초과하지 않는 경우 무조건 시간복잡도 초과
# (무게, 가치) 로 정렬한다면?
# 무게가 같은 것끼리 묶어놓은 후 해당 무게가 불가능하다면 바로 다음 무게로 넘어갈 수 있다

