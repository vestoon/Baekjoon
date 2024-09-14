import sys
input = sys.stdin.readline

N = int(input())
M = 1 # Max length of tanghulu
fruits = list(map(int, input().split()))
used = [0 for x in range(10)]
used[fruits[0]] = 1

j = 0
curLen = 1
kinds = 1
for i in range(N):
    while kinds <= 2:
        M = max(M, curLen)

        if j == N-1:
            break
        j += 1
        curLen += 1
        if not used[fruits[j]]:
            kinds += 1
        used[fruits[j]] += 1
        
    used[fruits[i]] -= 1
    curLen -= 1
    if not used[fruits[i]]:
        kinds -= 1

print(M)