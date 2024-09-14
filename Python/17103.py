import sys
import math
input = sys.stdin.readline

isPrime = [True for x in range(1000001)]
isPrime[0] = False
primes = []
for i in range(2, 1001):
    if not isPrime[i]:
        continue
    
    primes.append(i)
    for j in range(i+i, 1000001, i):
        isPrime[j] = False
for i in range(1001, 1000001):
    if isPrime[i]:
        primes.append(i)

# print(primes)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    for p in primes:
        if p > N//2:
            break
        if isPrime[N-p]:
            cnt += 1
    
    print(cnt)
