N = input()  # str
M = int(input())  # 고장난 번호의 개수
if M:  # 고장난 번호가 존재한다면
    wrong = list( map( int, input().split() ) )  # 누를 수 없는 번호
else:
    wrong = []
direct = abs(100-int(N))  # 채널 직접 입력 안하고 100번에서 갈 때 눌려야 하는 횃수
available = [x for x in range(10) if x not in wrong]  # 누를 수 있는 번호
place = len(N)  # 목적 채널의 자릿수
upper = int(N)
lower = int(N)
# print(wrong)
if not available:  # 누를 수 있는 번호가 없다면 걍 100번부터 가야함
    print(direct)
    exit()

while True:
    if lower >= 0:
        for number in str(lower):
            if int(number) in wrong:
                break
        else:
            stopover = lower
            break
    for number in str(upper):
        # print('number: ', number)
        if int(number) in wrong:
            # print('wrong 에 있으므로 불가능')
            break  # 이러면 upper는 아직 갈 수 없는 채널이다
    else:  # 찾았다 요놈!
        stopover = upper
        # print('찾았다! stopover는 ', stopover)
        break

    upper += 1
    # print('upper: ', upper)
    lower -= 1
    # print('lower: ', lower)


ans = len(str(stopover)) + abs(int(N)-stopover)
# print("stopover: ", stopover)
# print(len(str(stopover)), abs(int(N)-stopover) )
print(min(direct, ans))  # 30퍼에서 틀림