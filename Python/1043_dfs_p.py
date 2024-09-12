import sys
# N: 사람의 수, M: 파티의 수
# 사람의 수는 1부터 센다
N, M = map(int, sys.stdin.readline().split())
truth_num, *truth_pp = map(int, sys.stdin.readline().split())  # 진실을 아는 사람의 수, 사람들 리스트
# pp_tf = [False for x in range(N+1)]  # 진실을 알고 있는 사람은 True 로 표시
pp_join = [[] for x in range(N+1)]  # 사람별로 참여할 수 있는 파티들의 리스트
pts = []  # 각각 파티마다 참여하는 사람들을 리스트로 저장
pp_visited = [False for _ in range(N+1)]
pts_lie = [True for x in range(M)]  # 거짓말을 할 수 있는 파티면 True
for i in range(M):
    party_num, *party = map(int, sys.stdin.readline().split())
    for p in party:
        pp_join[p].append(i)
    pts.append(party)


def dfs(people_i):  # 매개변수로 비밀을 알거나 알게 될 사람들이 들어감
    pp_visited[people_i] = True
    for party in pp_join[people_i]:  # 그 사람이 참석하는 파티들에 대해서
        pts_lie[party] = False  # 일단 그 파티는 거짓말을 할 수 없는 파티이고
        for nxt_people in pts[party]:  # 그 파티에 참석하는 사람들 중 방문하지 않은 모든 사람들에 대해 dfs
            if not pp_visited[nxt_people]:
                dfs(nxt_people)


for p in truth_pp:
    if not pp_visited[p]:
        dfs(p)

count = 0
for b in pts_lie:
    if b:
        count += 1
print(count)

