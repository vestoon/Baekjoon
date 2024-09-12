import sys
# N: 사람의 수, M: 파티의 수
N, M = map(int, sys.stdin.readline().split())
truth_num, *truth_people = map(int, sys.stdin.readline().split())  # 진실을 아는 사람의 수, 사람들 리스트
people = [False for x in range(N+1)]  # 진실을 알고 있는 사람은 True 로 표시
for p in truth_people:
    people[p] = True


parties = []  # 각각 파티마다 참여하는 사람들을 리스트로 저장
parties_lie = [True for x in range(M)]  # 거짓말을 할 수 있는 파티면 True
for _ in range(M):
    party_num, party = map(int, sys.stdin.readline().split())
    parties.append(party)

# 카운트를 만들어 놓고 거짓말을 할 수 없는 파티를 줄여가면서 계산해보자
count = M

# 일단 진실을 알고 있는 사람들이 있는 파티부터 걸러내자
# 진실을 알고있는 사람이 있는 파티에 참가한 사람들은 모두 진실을 알고 있는 것으로 처리하자
for i in range(M):
    party = parties[i]
    for p in party:
        if people[p]:
            parties_lie[i] = False
            break
    else:


# 결론: 이런 식으로는 겨우 두번의 탐색으로는 다 찾는다는걸 보장할 수 없다
#      갱신되는 파티가 없을 때까지 반복하면 가능할지도?

# 진실을 아는 사람들 마다 그래프 탐색을 해보자!
