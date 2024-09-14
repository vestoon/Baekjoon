import sys
input = sys.stdin.readline

T, K = map(int, input().split())


def enhance(cur_level: list ) -> int:
    diff = 0
    for i in range(5): # i 번째 스킬의 레벨을 내렸을 때
        if not cur_level[i]: # 레벨이 0이라 내릴 수 없으면 continue
            continue

        if len(level_info[i])-1 < cur_level[i]:
            minus = 0
        else:
            minus = level_info[i][cur_level[i]] - level_info[i][cur_level[i]-1] # i 번째 스킬을 내렸을 때의 감소량
        plus = 0 # j번째 스킬을 올렸을 때의 증가량
        for j in range(5):
            if i == j: # 같은 스킬을 올렸다 내리지 않음
                continue
            if len(level_info[j])-1 <= cur_level[j]:
                continue
            plus = max(plus, level_info[j][cur_level[j]+1] - level_info[j][cur_level[j]])
        
        diff = max(diff, plus-minus)
    return diff



# 스킬 정보 저장
level_info = [[0] for x in range(5)] # 레벨 증가, 감소 때 참조

for level_idx in range(5):
    inp = list(map(int, input().split()))
    for i in range(1, inp[0]+1): 
        level_info[level_idx].append(inp[i])

# print("레벨 정보")
# for _ in level_info:
#     print(_)

# 장비 정보 저장
equipments = [] # 머리, 상의, 하의 전부 저장

for _ in range(3):
    equip_num = int(input())
    equips = [[0, [0, 0, 0, 0, 0]]]
    prices = list(map(int, input().split()))
    for i in range(equip_num): 
        equips.append([prices[i]])
    for i in range(equip_num): 
        equips[i+1].append(list(map(int, input().split())))
    equipments.append(equips)

# print("장비 정보")
# for x in equipments:
#     for y in x:
#         print(y)
#     print()
# exit()
# 완탐 시작
M_attackPower = 0
for cur_head in equipments[0]:
    for cur_top in equipments[1]:
        for cur_bottom in equipments[2]:
            case_T = T - cur_head[0] - cur_bottom[0] - cur_top[0]
            if case_T < 0:
                continue

            cur_level = [cur_head[1][i]+cur_bottom[1][i]+cur_top[1][i] for i in range(5)]
            cur_attackPower = 0
            for i in range(5):
                cur_attackPower += level_info[i][min(len(level_info[i])-1, cur_level[i])]

            if case_T >= K:
                cur_attackPower += enhance(cur_level)
            
            # if cur_attackPower == 26:
            #     print("선택")
            #     print(cur_head, cur_top, cur_bottom, sep ="\n")
            #     print("현재 레벨")
            #     print(cur_level)
            #     print("강화", enhance(cur_level))

            M_attackPower = max(M_attackPower, cur_attackPower)
            

print(M_attackPower)


