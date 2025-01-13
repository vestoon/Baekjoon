import sys
input = sys.stdin.readline

isPrime = [True for x in range(100001)]
for i in range(2, 401):
    if not isPrime: continue
    for nxt in range(i*2, 100001, i):
        isPrime[nxt] = False
# isPrime 구현 완료


while True:
    inp = input().rstrip()
    if inp == '0': break
    ans = 0

    # 길이가 l 이고 소수인 부분 문자열이 있는지 탐색
    for l in range(min(len(inp), 5), 0, -1):

        for i in range(len(inp)-l + 1):
            cur = int(inp[i:i+l])
            if isPrime[cur]:
                ans = max(ans, cur)
            
        # # 현재 길이에서 이미 찾았다면 더 짧은 길이에서 찾지 않고 종료
        # if findPrime:
        #     print(ans)
        #     break
    print(ans)



"""
테게 반복 1000
찾을 수 있는 소수의 범위 2 ~ 100000

"""