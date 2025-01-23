import sys
input = sys.stdin.readline
isPrime = [True for x in range(119)]
isPrime[0] = False
isPrime[1] = False
# isPrime 초기화
for i in range(2, 12):
    if not isPrime[i]: continue

    for nxt in range(i+i, 119, i):
        isPrime[nxt] = False
    
# canMake 초기화
canMake = [False for x in range(119)]
for i in range(2, 119):
    if not isPrime[i]: continue

    # i가 소수인 경우 두 번째 소수인 j를 탐색
    for j in range(i, 119):
        if not isPrime[j]: continue

        if i+j < 119:
            canMake[i+j] = True

N = int(input())
for _ in range(N):
    a = int(input())

    print("Yes" if canMake[a] else "No")