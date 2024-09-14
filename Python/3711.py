import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    G = int(input())
    sn = [int(input()) for x in range(G)]

    m = G
    while True:
        visited = set()

        for s in sn:
            if s%m in visited:
                break
            else:
                visited.add(s%m)
        else:
            break
        
        m += 1
    print(m)

