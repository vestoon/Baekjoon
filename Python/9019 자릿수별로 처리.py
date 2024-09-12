import sys
import collections
T = int(sys.stdin.readline())


def D(n):  # 여기서는 n 이 각 자리수를 담는 리스트 or 튜플
    ans = n
    ans[0] = (ans[0]*2)%10
    for i in range(1,3):
        if ans[i] <= 4:
            ans[i] = 2*ans[i]
        else:
            ans[i-1] += 1
            ans[i] = (2*ans[i]) % 10
    return ans


def S(n):
    ans = n
    i = 3
    while i <= 0:
        if ans[i]:
            ans[i] -= 1
            break
        ans[i] = 9
        i -= 1
    else:
        return 0
    return ans


def L(n):
    ans = n
    ans.append(ans.pop(0))
    return ans


def R(n):
    ans = n
    ans.insert(0, ans.pop())
    return ans


for test_case in range(T):
    # print('test_case:', test_case+1)
    visited = [0 for x in range(10000)]
    A, B = map(int, sys.stdin.readline().split())  # 여기서 BFS 돌려봐야 할듯? visited 를 사용하는게 좋을까?
    a, b = [0 for x in range(4)], [0 for x in range(4)]
    for x in range(4):
        i = 3-x
        a[i] = A % 10
        A = A//10
        b[i] = B % 10
        B = B//10

    front = [a, '']  # (숫자, 경로) 형태로 큐에 넣어서 탐색할까?
    BFS = collections.deque()

    while front[0] != b:
        # print('front[1]:', front[1])
        if not front[0]:
            continue
        n = front[0]
        path = front[1]
        d = D(n); s = S(n); l = L(n); r = R(n)
        if not visited[d]:
            BFS.append([d, path+'D'])
            visited[d] = True
        if not visited[s]:
            BFS.append([s, path + 'S'])
            visited[s] = True
        if not visited[l]:
            BFS.append([l, path + 'L'])
            visited[l] = True
        if not visited[r]:
            BFS.append([r, path + 'R'])  # 이거 반복좀 줄일 수 있는 방법이 없나
            visited[r] = True
        front = BFS.popleft()
    print(front[1])





