"""
그냥 완탐하세여

1. n번째 항의 길이를 기준으로 모든 경우의 수 계산 
2. n번째 항의 길이가 l1일 때 가능한 n-1번째 항 찾기
(여기서 n-1번째 항의 길이를 기준으로 완탐, n번째 항의 약수를 기준으로 존재하는지 탐색하면 시간 초과다)
3. n-1번째 항의 길이가 l2일 때 1 ~ n-1 번째 항까지의 수열이 등차수열일 수 있는지 탐색
4. 등차수열이 존재하는지 확인하려면 또 n-1번째 항을 기준으로 가능한 모든 n-2번째 항을 탐색한다. 똑같이 길이를 기준으로 탐색
5. n-2번째 항을 구함으로써 공차 d가 확정되면 찾고자 하는 다음 항을 수열이 사라질 때까지 계속 빼주면서 확인한다.
당연히 찾고자 하는 항에도 공차를 계속 빼줘야 하고 여기서 여러 디테일이 필요하다.

역할별로 함수를 자세히 만들어 놨으니 참조
"""

def sol():
    S = input().rstrip()
    L = len(S) # 3 <= L <= 2348
    ret = -1 # 최소값 구하기

    for l in range(1, min(L-2, 9)+1): # l: 마지막 항의 길이, 나머지 두 항의 길이가 최소 2는 돼야 하므로 L-2
        rest, last = S[:-l], S[-l:] # 1~n-1 항, 제일 마지막 항
        if last[0] == '0': continue # 마지막 항의 제일 왼쪽이 0인 경우 올바른 파싱이 아님

        tmp, prev = find_Fa(rest, last) # last가 마지막 항일 때의 가능한 작은 Fa
        if tmp != -1: # Fa가 존재하는 경우
            prev = str(prev)
            rest = rest[:-len(prev)] # 1 ~ n-2 번째 항까지로 변경
            # print('->', rest, prev)
            if find_d(rest, prev):
                ret = min(ret, tmp) if ret != -1 else tmp# 최종
    
    return 0 if ret == -1 else ret

# 마지막 항이 last일 때 나올 수 있는 최소한의 Fa 반환
def find_Fa(rest:str, last:str) -> int:
    L = len(last)
    last = int(last) # 마지막 항을 정수로 변환

    for l in range(min(L, len(rest)-1), 0, -1): # 길이가 긴 것부터 봐야 제일 작은 Fa부터 탐색 가능
        # print('l', l)
        prev = rest[-l:] # n-2 번째 항
        if prev[0] == '0': continue
        prev = int(prev)

        if last%prev == 0 and prev != last:
            return (last//prev, prev) # 계산된 Fa 와 그에 따른 n-1번째 항인 prev 반환

    return (-1, 0) # 존재하지 않는 경우

# 마지막 항이 last이고 그 앞이 rest인 등차수열이 존재하는지 bool을 리턴
# 여기서 rest1안에 최소한 2개의 항이 있어야 한다
def find_d(rest1:str, last:str) -> bool: # 여기서 last는 n-1번째 항
    for l in range(1, min(len(rest1), len(last))+1): # l: n-2번째 항의 길이
        # 여기서부터 rest2는 길이가 0일 수도 있다
        rest2, prev = rest1[:-l], rest1[-l:] # prev: n-2번째 항
        if prev[0] == '0': continue


        # 이제 공차를 구하면서 본격적으로 검사
        if int(last) <= int(prev): continue # 공차가 존재하지 않으면 패스

        d = int(last) - int(prev)
        if check_d(rest2, int(prev), d):
            return True
    
    return False

# rest+last가 last를 마지막 항으로 하는 공차가 d인 수열인지를 확인해주는 함수
def check_d(rest:str, last:int, d:int) -> bool:
    target = last-d # 현재 rest에서 찾아야 할 문자열
    while rest:
        if target <= 0:
            return False
        l = len(str(target))
        if rest[-l:] != str(target):
            return False

        rest = rest[:-l]
        target -= d
        
    return True

print(sol())