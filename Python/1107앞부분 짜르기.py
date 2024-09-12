N = input()  # str
M = int(input())  # 고장난 번호의 개수
if M:  # 고장난 번호가 존재한다면
    wrong = list( map( int, input().split() ) )  # 누를 수 없는 번호
else:
    wrong = []
direct = abs(100-int(N))  # 채널 직접 입력 안하고 100번에서 갈 때 눌려야 하는 횃수
available = [x for x in range(10) if x not in wrong]  # 누를 수 있는 번호
place = len(N)  # 목적 채널의 자릿수
ans = 0
for i in range(place):  # 일단 앞자리부터 누를수 있는건 눌러보자, 어디서부터 누를 수 없는 번호가 나오는지 탐색
    if int(N[i]) in wrong:
        break  # index 찾음
else:  # 문제 없이 전부 입력할 수있는 경우
    # print('문제 없음!')
    print(min(place, direct))
    exit()
ans += i
N = N[i:]  # 첫 자리부터 틀린 수로 변환
place = len(N)
n = int(N[0])  # 제일 앞 자리수
err = 0  # <-------------------------------------------- NameError 가 뜨는거 보니 밑의 반복문에서 한번도 안걸리는 경우가 있는듯
for x in range(1, max(10-n, n+1)):
    lower = n - x
    upper = n + x
    lowererr = 500000
    uppererr = 500000
    if (lower in available) or (upper in available):  # iterator 문제는 아니고 요 조건 분기에 안걸리는 경우가 있다고?
        if lower in available:  # 위에서 찾은 경우
            # print("find at lower")
            nearest = int(str(lower)+str(available[-1])*(place-1))
            lowererr = int(N) - nearest
            # print("nearest:", nearest, 'lowererr: ', lowererr)
        if upper in available:  # 아래에서 찾은 경우
            nearest = int(str(upper) + str(available[0]) * (place - 1))
            # print("find at upper")
            uppererr = nearest - int(N)
            # print("nearest:", nearest, 'uppererr: ', uppererr)
        err = min(lowererr, uppererr)
        # print('err =', err)
        ans += err
        break
else:
    ans = direct

print(min(ans, direct))  # ?? 한 10퍼 찍기 전에 틀림



