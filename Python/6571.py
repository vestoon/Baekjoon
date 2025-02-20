import sys
input = sys.stdin.readline

"""
a <= fi <= b 인 피보나치 수의 개수 구하기기
이분탐색 쓰면 위치는 찾을 수 있긴 한데
문제는 10*100 까지 메모리에 저장 할 수도 없다.

f1, f2 = 1, 2
f1, f2 = f2, f1+f2
"""


def sol():
    while True:
        a, b = map(int, input().split()) # a, b 는 음이 아닌 정수
        if a == 0 and b == 0: return 
        if b == 1: # 예외
            print(1)
            continue

        cnt = 1 if a < 2 else 0 # 예외, f2 가 항상 2에 맞춰진 상태로 시작하기 때문
        f1, f2 = 1, 2

        while f2 < a:
            f1, f2 = f2, f1+f2
        
        while f2 <= b:
            cnt += 1
            f1, f2 = f2, f1+f2
        
        print(cnt)

sol()