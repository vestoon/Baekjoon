T = int(input())


def count_case(target):
    count = 0

    def rec(acc):
        nonlocal count
        if acc > target:
            return
        elif acc == target:
            count += 1
        elif acc < target:
            for x in range(1, 4):
                rec(acc+x)

    rec(0)

    return count


for case in range(T):
    n = int(input())
    print(count_case(n))
