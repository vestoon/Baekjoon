from queue import Queue
x, y = map(int, input().split())

ans = 0
visited = [False for x in range(100001)]
BFS = Queue()
BFS.put(x)
find = False
nxtL = 1

while not find:
    L = nxtL
    nxtL = 0
    # print("len: ", L)  #
    for t in range(L):
        cur = BFS.get()
        # print('cur: ', cur)  #
        if cur == y:
            print(ans)
            find = True
            break
        for nxt in [cur-1, cur+1, cur*2]:
            if 0 <= nxt <= 100000:
                if visited[nxt]:
                    continue
                else:
                    visited[nxt] = True
                    BFS.put(nxt)
                    nxtL += 1
    ans += 1


