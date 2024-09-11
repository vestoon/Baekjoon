i = input()
i = i.split('-')   # ['3+5', '4+6', '3+5']
plus = i[0]   # 1+2+3+
minus = i[1:]  # 3+5+3-5
# print(plus)
# print(minus)
# minus = minus.replace('+', '-')
ans = 0


for x in plus.split('+'):
    ans += int(x)

for poly in minus:
    for x in poly.split('+'):
        ans -= int(x)

print(ans)









