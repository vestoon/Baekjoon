import sys
import collections
T = int(sys.stdin.readline())
for test_case in range(T):
    cmds = sys.stdin.readline().rstrip()  # ex RDD
    n = int(sys.stdin.readline())  # 배열의 길이
    if n:
        ac = sys.stdin.readline()
        ac = list(map(int, ac[1:-2].split(',')))
    else:
        sys.stdin.readline()
        ac = []

    dq = collections.deque()
    for x in ac:  # 원소들을 전부 덱에 넣는다
        dq.append(x)

    reverse = -1  # 1 이면 뒤집힌거
    for cmd in cmds:  # 함수 실행
        if cmd == 'R':
            reverse *= -1
        elif cmd == 'D':
            if not dq:
                print("error")
                break
            elif reverse == 1:
                dq.pop()
            elif reverse == -1:
                dq.popleft()
    else:  # 에러가 뜨지 않은 경우 남은 배열을 출력
        if dq:
            print('[', end='')
            if reverse == 1:
                while len(dq) != 1:
                    print(dq.pop(), ',', sep='', end='')
                print(dq.pop(), ']', sep='')
            elif reverse == -1:
                while len(dq) != 1:
                    print(dq.popleft(), ',', sep='', end='')
                print(dq.popleft(), ']', sep='')
        else:
            print('[]')

