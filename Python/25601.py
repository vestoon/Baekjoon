import sys
input = sys.stdin.readline

N = int(input())
parent = {}

def isCast(x, y):
    cur = x
    while True:
        # cur이 루트인 경우 종료
        if cur not in parent:
            break

        cur = parent[cur]
        if cur == y:
             return True

    cur = y    
    while True:
        if cur not in parent:
            break

        cur = parent[cur]
        if cur == x:
            return True
    return False

for _ in range(N-1):
    A, B = input().split()
    parent[A] = B

x, y = input().split()
print( 1 if isCast(x, y) else 0)