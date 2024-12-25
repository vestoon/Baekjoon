inp = list(map(int, input().split()))
win_rate = [[0 for x in range(8)] for y in range(8)]
i = 0
for p in range(7, 0, -1):
    # 7 6 5 4 3 2 1
    # 플레이어 번호: 7-p
    for op in range(8-p, 8):
        win_rate[7-p][op] = inp[i]/100
        win_rate[op][7-p] = 1 - inp[i]/100
        i += 1

# for x in win_rate:
#     for xx in x:
#         print(xx, end='\t')
#     print()

final_win_rate = [0 for x in range(8)]
"""
8강, 4강, 결승별로 함수를 따로 만들어서 재귀 호출해 보자
매개변수 players 안에서 반복을 돌라는 걸로
"""
def match8(players, cur, nxt, prob):
    if cur == 8:
        match4(nxt, 0, [], prob)
        return 
    
    match8(players, cur+2, nxt+[players[cur]], prob*win_rate[players[cur]][players[cur+1]])
    match8(players, cur+2, nxt+[players[cur+1]],  prob*win_rate[players[cur+1]][players[cur]])

def match4(players, cur, nxt, prob):
    if cur == 4:
        match2(nxt, prob)
        return

    match4(players, cur+2, nxt+[players[cur]], prob*win_rate[players[cur]][players[cur+1]])
    match4(players, cur+2, nxt+[players[cur+1]], prob*win_rate[players[cur+1]][players[cur]])

def match2(players, prob):
    final_win_rate[players[0]] += prob*win_rate[players[0]][players[1]]
    final_win_rate[players[1]] += prob*win_rate[players[1]][players[0]]

match8([x for x in range(8)], 0, [], 1)
print(*final_win_rate)