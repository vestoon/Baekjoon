import sys

T = int(sys.stdin.readline())
for g in range(T):
    n, target = map(int, sys.stdin.readline().split())  # 타겟은 0부터 센 인덱스
    importance = list(map(int, sys.stdin.readline().split()))
    queue = [(x, importance[x]) for x in range(n)]
    flag = True
    count = 0  # 뽑은 횃수

    while flag:
        # print(queue)
        for d in queue[1:]:
            if d[1] > queue[0][1]:
                queue.append(queue.pop(0))
                break
        else:
            count += 1
            if queue[0][0] == target:
                flag = False
            queue.pop(0)
    print(count)
