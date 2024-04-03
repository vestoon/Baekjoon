
N = int(input())

nfact = 1
for x in range(1, N + 1):
    nfact *= x

count = 0
for s in str(nfact)[-1:0:-1]:
    if s == '0':
        count += 1
    else:
        break

print(count)
