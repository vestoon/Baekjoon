X, Y = map(int, input().split())
if X == Y:
    print(-1)
    exit()

Z = Y*100 // X
if Z == 99:
    print(-1)
    exit()

numer = X*(1+Z) - 100*Y
denom = 99 - Z


q = numer//denom
if numer % denom:
    q += 1

print(q)

