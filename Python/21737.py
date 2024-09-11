import sys
input = sys.stdin.readline

N = int(input())
formula = input().rstrip()
noOutput = True
operand = 0
acc = 0
operator = 'P'


def cal():
    global acc, operand
    if operator == 'S':
        acc -= operand
    elif operator == 'M':
        acc *= operand
    elif operator == 'P':
        acc += operand
    elif operator == 'U':
        if acc > 0:
            acc //= operand
        else:
            acc *= -1
            acc //= operand
            acc *= -1

    operand = 0
    return


for n in formula:
    # print('n', n)
    if n.isdigit():
        operand *= 10
        # print(operand)
        operand += int(n)
    else:
        if n == 'C':
            noOutput = False
            cal()
            print(acc, end=' ')
        elif operator != 'C':
            cal()
        operator = n

if noOutput:
    print("NO OUTPUT")
