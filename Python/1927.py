import sys

N = int(sys.stdin.readline().rstrip())
minHeap = [0]
for g in range(N):
    # print('minHeap:', minHeap)
    x = int(sys.stdin.readline().rstrip())  # 트리에 실행시킬 명령어
    # print('x:', x, end=' ')
    if x:  # x 가 0 이 아니면
        minHeap.append(x)  # 일단 끝에 추가
        i = len(minHeap)-1  # 맨 끝 인덱스부터 탐색 업힙 시작
        while minHeap[int(i/2)] > minHeap[i]:  # 부모 노드보다 값이 작다면
            minHeap[int(i/2)], minHeap[i] = minHeap[i], minHeap[int(i/2)]  # 교체해준다
            i = int(i/2)
    else:
        if len(minHeap) == 1:
            print(minHeap[0])
            # print('l:', l)
            continue
        if len(minHeap) == 2:
            print(minHeap[-1])
            minHeap.pop(-1)
            continue
        print(minHeap[1])
        # print('?', minHeap)
        minHeap[1] = minHeap.pop(-1)
        i = 1
        while 2*i <= len(minHeap)-1:
            if 2*i == len(minHeap)-1:
                # print('case 1')
                if minHeap[i] > minHeap[i*2]:
                    minHeap[i*2], minHeap[i] = minHeap[i], minHeap[i*2]
                    i = i*2
                    continue
            elif minHeap[i] > min(minHeap[i*2], minHeap[i*2 +1]):
                if minHeap[i*2] > minHeap[i*2 + 1]:
                    # print('case 2')
                    minHeap[i * 2 + 1], minHeap[i] = minHeap[i], minHeap[i * 2 + 1]
                    i = i*2 + 1
                    continue
                else:
                    # print('case 3')
                    minHeap[i * 2], minHeap[i] = minHeap[i], minHeap[i * 2]
                    i = i*2
                    continue
            break
    # print(minHeap)


