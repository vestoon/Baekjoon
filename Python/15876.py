# n: 사람 수, k: 진수의 차례
n, k = map(int, input().split())
k -= 1

cnt = 0 # 진수가 숫자를 외친 횟수
cur = 0 # 현재 숫자를 외쳐야 하는 사람이 누구인지
cur_num = 0 # 현재 사용하고 있는 숫자


while cnt != 5:
    
    cur_str = bin(cur_num)[2:] # 현재 사용하고 있는 숫자를 이진수로 바꾼 문자열
    for i in cur_str:
        # 진수가 외칠 차례라면
        if cur == k:
            print(i, end=' ')
            cnt += 1
            if cnt == 5: break
        
        # cur 증가
        cur = (cur+1)%n
    cur_num += 1