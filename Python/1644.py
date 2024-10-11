N = int(input())

"""
N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수 출력하기, 연속된 소수엔 자기 자신도 포함
N  <= 4,000,000
1~2,000 까지 계속 나눴을때 맥시멈 2,000,000
일단 소수는 규칙을 찾을 수가 없기 때문에 N까지는 무조건 찾아 놔야 한다. 
찾아서 리스트로 만드는데 최소 O(N) 소모 ㅠㅠ

아차차 연속된 소수가 총 몇 개인지는 모른다. -> 투 포인터 사용?
"""
ans = 0
numbers = [x for x in range(N+1)]
primes = []
numbers[1] = 0
for i in range(2, N):
    if i**2 > N:
        break

    tmp = i*2
    while tmp <= N:
        numbers[tmp] = 0
        tmp += i

for i in range(2, N+1):
    if numbers[i]:
        primes.append(i)

if not primes:
    print(0)
    exit()
j = 0
sSum = primes[0]
l = len(primes)


for i in range(l):

    if sSum < N:
        while sSum < N and j < l-1:
            j += 1
            sSum += primes[j]

    if sSum == N:
        ans += 1
    sSum -= primes[i]

print(ans)