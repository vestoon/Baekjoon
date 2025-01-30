import sys
input = sys.stdin.readline

"""
일단 밥이 가진 가장 작은 수를 설정

앞 자리수마다 돌면서
같은 경우: 계속
작은 카드가 있는 경우: 이후는 최대값으로 채움
큰 카드밖에 없는 경우: 그 자리를 비우고 이우를 최대값으로 채움

완벽히 똑같은 카드를 맞출 수 있는 경우에는 어떻게 해야 할까? 
제일 뒤에 두 자리 수를 바꾸거나 그래도 불가능하다면 한 자리 수를 빼야 할 지도
한 자리를 빼야 한다면 그 자리에서 그냥 낼미차순 정렬 해야 한다. 

아니지 아니지
밥이 만든 수는 n 자리수이기 때문에 n-1 자리수인 수는 무조건 밥이 이길 수 밖에 없다. 
이때 만들 최대값을 고정적인 알고리즘으로 구할 수 있다. 


1534
1435

따라할 수 있는 부분까지는 따라하다가 더 작아지는 시점부터는 내 마음대로
하지만 끝까지 완벽하게 똑같다면? -> 애초에 무작정 최대한 큰 수만 넣는 건 최선이 아니다.

"""
# n 자리 숫자를 만들 수 있는지 탐색, 안되면 n-1로 따로 함수 만들어서 찾자
def backtracking(cur:int):
    global ans
    if cur == n:
        return int(ans) < int(Bob_min)


    for i in range(9, 0, -1):
        if not Alice_card[i]: continue
        if int(Bob_min[cur]) < i: continue
        
        if int(Bob_min[cur]) == i:
            # 자릿수랑 딱 맞는 숫자가 있는 경우
            ans += str(i)
            Alice_card[i] -= 1
            if backtracking(cur+1):
                return True
            ans = ans[:-1]
            Alice_card[i] += 1
        else:
            # 자릿수보다 더 작은 수를 쓰게 되는 경우
            # 나머지는 최대값으로 채우고 종료해야 한다. 
            ans += str(i)
            Alice_card[i] -= 1
            for r in range(9, 0, -1):
                while Alice_card[r]:
                    ans += str(r)
                    Alice_card[r] -= 1
            return True

    
    return False




T = int(input())
for tc in range(1, T+1):
    n = int(input())
    Bob = input().rstrip()
    Bob_min = str(min(int(Bob), int(Bob[::-1])))
    Alice = input().rstrip()
    Alice_card = [0 for x in range(10)] # 앨리스가 가진 카드의 개수
    for x in Alice:
        Alice_card[int(x)] += 1
    

    # print("Bob:", Bob_min)
    ans = ""
    if backtracking(0):
        print(ans)
    else:
        ans = ""
        for i in range(9, 0, -1):
            while Alice_card[i]:
                ans += str(i)
                Alice_card[i] -= 1
        print(ans[:-1])
    