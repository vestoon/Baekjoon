
# (결과값, 캐리) 여부 반환
def adder(x:int, y:int, carry:bool) -> tuple:
    ret_value = x + y + 1 if carry else x + y
    ret_carry = True if 16 <= ret_value else False
    return (ret_value%16, ret_carry)

# 0 ~ 15
used = [False for x in range(16)] # 0 부터 15까지 배정 했는지 안했는지
h = {'L':-1, 'I':-1, 'S':-1, 'T':-1, 'F':-1, 'O':-1, 'A':-1, 'C':-1, 'K':-1} # 각 알파벳에 대한 hash 값

# 1의 자리부터 계산 순서
cal = [('T', 'O'), ('S', 'L'), ('I', 'I'), ('L', 'F')]
ans = ['K', 'C', 'A', 'T', 'S'] # 계산 정답 1의 자리부터
equations = []

# i: 몇 번째 자리를 계산하는 중인지 , carry: 이전 계산에서 carry가 발생했는지
def simulation(i:int , carry: bool):
    if i == 4:
        if carry:
            check_ans()
        return # base case

    cases = [] # 정의할 경우의 수를 숫자 튜플로 저장
    a, b = cal[i] # 둘 다 알파벳

    # a 를 아직 used 같은데 기록하지 않는다. cases에서 사용할 때에 기록하자자
    if h[a] != -1 and h[b] == -1: # b만 정의해야 하는 경우
        for nb in range(16):
            if used[nb]: continue
            
            cases.append((h[a], nb))
    elif h[b] != -1 and h[a] == -1: # a만 정의해야 하는 경우
        for na in range(16):
            if used[na]: continue

            cases.append((na, h[b]))
    elif h[a] == -1 and h[b] == -1: # a와 b가 둘 다 정의되어있지 않은 경우
        if a == b: # a와 b 가 같은 'I'의 경우
            for d in range(16):
                if not used[d]:
                    cases.append((d, d))
        else: # 할당해야 할 a와 b가 다른 경우
            for na in range(16): 
                for nb in range(16):
                    if na == nb or used[na] or used[nb]: continue

                    cases.append((na, nb))
    else: # a와 b가 이미 다 정해져 있는 경우
        cases.append((h[a], h[b]))
    
    for case in cases: 
        # 이 부분에서 문제가 생긴다. 새로 할당된 값만 되돌려야 하는데...
        # 원래 정의된 값까지 같이 원상복구시켜서 문제
        tmps = [ x for x in case if used[x] == False] # 임시로 일단 할당해 볼 것들을 정의
        x, y = case # a, b에 숫자 x, y를 할당하는 경우
        h[a] = x
        h[b] = y
        used[x] = True
        used[y] = True

        ret_value, ret_carry = adder(x, y, carry)
        if h[ans[i]] != -1: # 계산 결과값의 hash값이 이미 정의된 상태라면
            if ret_value == h[ans[i]]:
                simulation(i+1, ret_carry)
        else: # 정의되지 않았다면 정의하고 계산 후에 원상복구
            if not used[ret_value]: # 새로 ans[i] 의 값이 이미 사용중이어선 안된다
                h[ans[i]] = ret_value
                used[ret_value] = True
                simulation(i+1, ret_carry)
                h[ans[i]] = -1 # 다시 원상복구구
                used[ret_value] = False

        if x in tmps:
            h[a] = -1
            used[x] = False
        if y in tmps:
            h[b] = -1
            used[y] = False
        # h[a] = -1
        # h[b] = -1
        # used[x] = False
        # used[y] = False


# 계산한 값이 맞으면 출력하는 함수
def check_ans():
    if h['L'] == 0 or h['F']== 0 or h['S'] != 1:
        return
    
    eq = ''
    for s in "LIST":
        eq += hex(h[s])[2:]
    eq += " + "

    for s in "FILO":
        eq += hex(h[s])[2:]
    eq += " = "

    for s in "STACK":
        eq += hex(h[s])[2:]
    equations.append(eq)

simulation(0, False)
equations.sort()
for eq in equations:
    print(eq)