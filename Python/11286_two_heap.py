import sys
N = int(sys.stdin.readline())
p_heap = [0 for x in range(200001)]  # 양수는 최소 힙
n_heap = [0 for x in range(200001)]  # 음수는 최대 힙
p_heap_size = 0
n_heap_size = 0


def p_upHeap(n):
    global p_heap_size
    p_heap_size += 1
    p_heap[p_heap_size] = n
    i = p_heap_size
    while p_heap[i] < p_heap[i//2]:
        p_heap[i], p_heap[i//2] = p_heap[i//2], p_heap[i]
        i = i//2
        if i == 1:
            break


def p_downHeap():
    global p_heap_size
    p_heap[1] = p_heap[p_heap_size]
    p_heap[p_heap_size] = 0
    if p_heap_size:
        p_heap_size -= 1 if p_heap_size else 0
    i = 1
    while p_heap[i*2]:
        if p_heap[i*2 + 1] and p_heap[i] > min(p_heap[i*2], p_heap[i*2 + 1]):  # 자식 노드가 둘 다 있을 때
            if p_heap[i*2] < p_heap[i*2 + 1]:
                p_heap[i*2], p_heap[i] = p_heap[i], p_heap[i*2]
                i = i*2
            else:
                p_heap[i*2 + 1], p_heap[i] = p_heap[i], p_heap[i*2 + 1]
                i = i*2 + 1
        elif p_heap[i] > p_heap[i*2]:  # 자식 노드가 하나만 있을 때
            p_heap[i], p_heap[i*2] = p_heap[i*2], p_heap[i]
            i = i*2
        else:
            break


def n_upHeap(n):
    global n_heap_size
    n_heap_size += 1
    n_heap[n_heap_size] = n
    i = n_heap_size
    while n_heap[i] > n_heap[i//2]:
        n_heap[i], n_heap[i//2] = n_heap[i//2], n_heap[i]
        i = i//2
        if i == 1:
            break


def n_downHeap():
    global n_heap_size
    n_heap[1] = n_heap[n_heap_size]
    n_heap[n_heap_size] = 0
    if n_heap_size:
        n_heap_size -= 1 if n_heap_size else 0
    i = 1
    while n_heap[i * 2]:
        if n_heap[i * 2 + 1] and n_heap[i] < max(n_heap[i * 2], n_heap[i * 2 + 1]):  # 자식 노드가 둘 다 있을 때
            if n_heap[i * 2] > n_heap[i * 2 + 1]:
                n_heap[i * 2], n_heap[i] = n_heap[i], n_heap[i * 2]
                i = i * 2
            else:
                n_heap[i * 2 + 1], n_heap[i] = n_heap[i], n_heap[i * 2 + 1]
                i = i * 2 + 1
        elif n_heap[i] < n_heap[i * 2]:  # 자식 노드가 하나만 있을 때
            n_heap[i], n_heap[i * 2] = n_heap[i * 2], n_heap[i]
            i = i * 2
        else:
            break


for oper in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        p_upHeap(x)
    elif x < 0:
        n_upHeap(x)
    # x == 0 일때 힙에서 원소를 뺀다
    elif p_heap_size and n_heap_size:
        if p_heap[1] < -1*n_heap[1]:
            print(p_heap[1])
            p_downHeap()
        else:
            print(n_heap[1])
            n_downHeap()
    elif p_heap_size:  # 양수 힙만 남아있는 경우
        print(p_heap[1])
        p_downHeap()
    else:  # 음수 힙만 남아있거나 둘 다 비어있는 경우
        print(n_heap[1])
        n_downHeap()




