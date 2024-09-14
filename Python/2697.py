import sys
input = sys.stdin.readline

"""
문자열 자체에서 오름차순이 되는 가장 오른쪽 부분을 찾는다 -> 없다면 biggest
시작 부분을 똑 떼고 바로 다음 큰 수를 넣은 다음 그 뒤를 오름차순으로 정렬하면 끝
"""

T = int(input())
for _ in range(T):
    inp = input().rstrip()
    inp = list(map(int, inp))

    for i in range(len(inp)-1, 0, -1):
        if inp[i-1] < inp[i]:
            break
    else:
        print("BIGGEST")
        continue

    i -= 1
    j = i
    ii = 10 # i 번째보다 바로 다음 큰 수
    for nxt in range(i+1, len(inp)):
        if inp[i] < inp[nxt] < ii:
            j = nxt
            ii = inp[j]
    
    # print(inp) # 바꾸기 전
    # 둘의 위치를 바꿔준다
    inp[i], inp[j] = inp[j], inp[i]
    inp[i+1:] = sorted(inp[i+1:])
    # print(inp) # 바꾼 후
    for x in inp:
        print(x, end='')
    print()
    