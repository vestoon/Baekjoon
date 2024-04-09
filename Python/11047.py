N, K = map(int, input().split())
coin = []
count = 0

for x in range(N):
    coin.append(int(input()))

for x in coin[-1:-N-1:-1]:
    count += K//x
    K %= x

print(count)
