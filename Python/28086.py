from collections import deque
inp = input().rstrip()

left = []
right = []
opers = ['+', '-', '*', '/']

i = 0
for i in range(1, len(inp)):
    if inp[i] in opers:
        break

left = inp[:i]
right = inp[i+1:]

leftNum = 0
rightNum = 0

for l in left:
    if l == '-': continue
    leftNum *= 8
    leftNum += int(l)

for r in right:
    if r == '-': continue
    rightNum *= 8
    rightNum += int(r)

if right[0] == '-':
    rightNum *= -1
if left[0] == '-':
    leftNum *= -1


ans = 0
oper = inp[i]
if rightNum == 0 and oper == '/':
    print("invalid")
    exit()

if oper == '+':
    ans = leftNum + rightNum
elif oper == '-':
    ans = leftNum - rightNum
elif oper == '*':
    ans = leftNum * rightNum
else:
    ans = leftNum // rightNum


ans8 = deque()
if ans < 0:
    print('-', end='')
    ans = abs(ans)
elif not ans:
    print(0)
    exit()

while ans:
    rest = ans%8
    ans8.append(rest)
    ans //= 8

while ans8:
    print(ans8.pop(), end='')


# print(51//-2)
"""
51 / 2 = 25
"""