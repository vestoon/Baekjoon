import sys
input = sys.stdin.readline


maxPrice = 0
maxValue = 0

people = []

N = int(input())
for _ in range(N):
    people.append(tuple(map(int, input().split())))
people.sort()

for price, delivery in people:
    value = 0

    for price2, delivery2 in people:
        if price <= price2 and price - delivery2 > 0:
            value += price - delivery2
    
    if value > maxValue:
        maxValue = value
        maxPrice = price

print(maxPrice)

