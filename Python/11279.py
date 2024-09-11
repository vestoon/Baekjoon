import sys
N = int(sys.stdin.readline())

def upHeap():
    i = size
    while heap[i] > heap[i//2]:
        heap[i], heap[i//2] = heap[i//2], heap[i]
        i = i//2
        if i == 1:
            return


def downHeap():
    i = 1
    while heap[i] < max(heap[i*2], heap[i*2 +1]):
        if heap[i*2] > heap[i*2 +1]:
            heap[i], heap[i*2] = heap[i*2], heap[i]
            i = i*2
        else:
            heap[i], heap[i*2 + 1] = heap[i*2 + 1], heap[i]
            i = i*2 + 1


heap = [0 for x in range(200001)]
size = 0
for cmd in range(N):
    x = int(sys.stdin.readline())
    # print('x:', x) #
    if x:
        heap[size+1] = x
        size += 1
        # print(heap) #
        if size > 1:
            upHeap()
        # print(heap) #
    else:
        print(heap[1])
        heap[1] = heap[size]
        heap[size] = 0
        if size:
            size -= 1
            downHeap()
        # print(heap) #










