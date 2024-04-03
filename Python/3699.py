import sys
T = int(sys.stdin.readline())
for test_case in range(T):
    # print("test_case:", test_case) #
    h, i = map(int, sys.stdin.readline().split())
    building = []
    for floor in range(h):
        building.append(list(map(int, sys.stdin.readline().split())))

    time = 0
    # x가 가로, y 가 세로
    car_num = 1
    while True:
        # print("car_num:", car_num) #
        for y in range(h):
            for x in range(i):
                # print('cor:', y, x)
                if building[y][x] == car_num:
                    time += y * 20
                    # print('time+', h*20) #
                    # x 가 i//2 보다 같거나 작으면 왼쪽으로 회전, 아니면 오른쪽으로 회전
                    if x <= i//2:
                        for rep in range(x):
                            building[y].append(building[y].pop(0))
                        time += x*5
                        # print('time+', x*5) #
                    else:
                        for rep in range(i-x):
                            front = building[y].pop()
                            building[y] = [front] + building[y]
                        time += (i-x) * 5
                        # print('time+', (i-x) * 5) #
                    car_num += 1
                    break
            else:
                continue
            break
        else:
            break
    print(time)

