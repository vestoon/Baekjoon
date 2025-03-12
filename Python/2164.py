N = int(input())

rest = [x for x in range(1, N+1)]

flag = 1 # 1일때 첫 번째 원소를 버린다다
while len(rest) != 1:
    l = len(rest)

    if flag == 1: # 짝수 번째 원소만 가져오기
        rest = [rest[i] for i in range(1, l, 2)]
    else: # flag == -1  : 홀수 번재 원소만 가져오기
        rest = [rest[i] for i in range(0, l, 2)]
    
    if l%2:
        flag *= -1

print(rest[0]) 