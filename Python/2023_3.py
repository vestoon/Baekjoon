import math
n = int(input())


def isPrime(n):
    for x in range(2, int(math.sqrt(n)) + 1):
        if not n % x:
            break
    else:
        return True
    return False


primeGraph = [[2, 3, 5, 7]]

while len(primeGraph) != n:
    newPrimeList = []
    for p in primeGraph[-1]:
        np0 = p*10
        for x in range(10):
            np = np0 + x
            if isPrime(np):
                newPrimeList.append(np)
    primeGraph.append(newPrimeList)

for y in primeGraph[-1]:
    print(y)


