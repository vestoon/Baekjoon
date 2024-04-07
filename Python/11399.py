N = int(input())

Pi = sorted(map(int, input().split()))
# print(Pi)
ans = 0
count = N
for x in Pi:
    ans += x*count
    count -= 1

print(ans)
