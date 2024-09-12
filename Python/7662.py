import sys
import heapq
T = int(input())


class DPQ:
    def __init__(self):
        self.visited = [False]*1000001
        self.min_heap = []
        self.max_heap = []

    def insert(self, num, q):
        heapq.heappush(self.min_heap, (num, q))
        heapq.heappush(self.max_heap, (num*-1, q))
        self.visited[q] = True

    def delete(self, flag):
        if flag > 0:  # 최대값 삭제
            while self.max_heap and not self.visited[self.max_heap[0][1]]:
                heapq.heappop(self.max_heap)
            if self.max_heap:
                self.visited[self.max_heap[0][1]] = False
                heapq.heappop(self.max_heap)
        elif flag < 0:
            while self.min_heap and not self.visited[self.min_heap[0][1]]:
                heapq.heappop(self.min_heap)
            if self.min_heap:
                self.visited[self.min_heap[0][1]] = False
                heapq.heappop(self.min_heap)

    def cur(self):
        while self.max_heap and not self.visited[self.max_heap[0][1]]:
            heapq.heappop(self.max_heap)
        while self.min_heap and not self.visited[self.min_heap[0][1]]:
            heapq.heappop(self.min_heap)
        if self.min_heap and self.max_heap:
            print(self.max_heap[0][0]*-1, self.min_heap[0][0])
        else:
            print("EMPTY")


for test_case in range(T):
    # print('test_case:', test_case)
    dpq = DPQ()
    K = int(sys.stdin.readline())
    for key in range(K):
        # print('key:', key)
        cmd = sys.stdin.readline().split()
        # print('cmd:', cmd)
        if cmd[0] == 'I':
            dpq.insert(int(cmd[1]), key)
        elif cmd[0] == 'D':
            flag = int(cmd[1])
            dpq.delete(flag)
    dpq.cur()

