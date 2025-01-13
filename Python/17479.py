import sys
input = sys.stdin.readline

# A: 일반 메뉴, B: 스페셜 메뉴, C: 서비스 메뉴
A, B, C = map(int, input().split())
menu_type = {} # name: type
menu_price = {} # name: price

# 일반 메뉴
for _ in range(A):
    food, price = input().split()
    menu_type[food] = "A"
    menu_price[food] = int(price)
# 스페셜 메뉴
for _ in range(B):
    food, price = input().split()
    menu_type[food] = "B"
    menu_price[food] = int(price)
# 서비스 메뉴
for _ in range(C):
    food = input().rstrip()
    menu_type[food] = "C"

N = int(input())
order_price = {'A': 0, 'B': 0}
c_order_cnt = 0

for _ in range(N):
    order = input().rstrip()
    type = menu_type[order]
    if type == 'C':
        c_order_cnt += 1
        continue

    price = menu_price[order]
    order_price[type] += price


if 1 < c_order_cnt:
    print("No")
elif order_price['B'] and order_price['A'] < 20000:
    print("No")
elif c_order_cnt and order_price['A'] + order_price['B'] < 50000:
    print("No")
else:
    print("Okay")
