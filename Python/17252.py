N = int(input())
if not N:
    print("NO")
    exit()

while N:
    r = N%3
    if r == 2:
        print("NO")
        break
    N -= r
    N //= 3
else:
    print("YES")