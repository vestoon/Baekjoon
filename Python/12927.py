inp = input().rstrip()
l = len(inp)
"""
YYYNYYYNYYYNYYNYYYYN -> 1 4 5 16
1 2 3 5 6 7 9 10 11 13 14 16 17 18 19 

4 8 12 15

15 16 20

16
제일 왼쪽 수부터 켜져있으면 계속 스위치를 누른다.

가정: 제일 왼쪽에 있는 불을 끄려면 그 숫자의 스위치를 누르는 것이 최선이다?
반례를 찾아보자
1. 그숫자보자 왼쪽에 있는 숫자의 스위치를 누르는 것이 최선인 경우가 있는가?

더 왼쪽에 있는 무언가를 누른다면? -> 최소한 그 숫자에는 불이 켜지기 때문에 이를 해결해야 하는 문제가 발생
하지만 뒤의 더 많은 불들을 꺼준다면? -> 의미가 없다. 왜냐 하면 뒤의 더 많은 문제를 해결해 봤자
그 작은 수를 해결하기 위해서 또 더 작은 수의 스위치를 눌러야 하기 때문
-> 이것까지 해결되는 반례가 있는지는 진짜 모르겠다...

"""

onoff = [True if inp[i] == 'Y' else False for i in range(len(inp))]
cnt = 0
for i in range(l):
    if onoff[i]:
        cnt += 1
        tmp = i
        while tmp < l:
            onoff[tmp] = False if onoff[tmp] else True
            tmp += i+1

print(cnt)