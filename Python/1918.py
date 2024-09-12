import collections

middle_expression = input()
stack_operand = collections.deque()
stack_operator = collections.deque()
priority_operator = {'+': 0, '-': 0, '*': 1, '/': 1, '(': -1, ')': 2}


def cal():
    global pre_priority
    right = stack_operand.pop()
    left = stack_operand.pop()
    operator = stack_operator.pop()
    stack_operand.append(left + right + operator)


pre_priority = -1
for op in middle_expression:
    if op.isalpha():
        stack_operand.append(op)
        continue

    # op 가 연산자일때
    if op == '(':
        pass
    elif op == ')':
        while stack_operator[-1] != '(':
            cal()
        stack_operator.pop()
        pre_priority = priority_operator[stack_operator[-1]] if stack_operator else -1
        continue
    elif priority_operator[op] == pre_priority:
        # 우선순위가 같을 때 한 번 계산
        cal()
    else:
        # 이전 값보다 더 우선순위가 낮은 연산자가 들어왔을 때
        # 현재 우선순위보다 더 낮은 연산자가 나오거나 스택이 빌 때까지 계산(여러번 계산할 수 도 있다.)
        # 이러한 경우 앞부분의 연산자들은 무조건 오름차순(단조증가)
        while pre_priority >= priority_operator[op]:
            cal()
            pre_priority = priority_operator[stack_operator[-1]] if stack_operator else -1
    # 우선순위가 높을 때는 그냥 추가하고 우선순위 최신화
    stack_operator.append(op)
    pre_priority = priority_operator[stack_operator[-1]]

# 나머지 쭉 계산
while len(stack_operand) != 1:
    cal()

print(stack_operand[0])