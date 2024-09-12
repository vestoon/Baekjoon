import sys
import collections
T = int(sys.stdin.readline())


def D(n):
    return (n*2) % 10000


def S(n):
    return n-1 if n else 9999


def L(n):
    left = n // 1000
    ans = n % 1000
    return ans*10 + left


def R(n):
    right = n % 10
    ans = n//10
    return ans + 1000*right


for test_case in range(T):
    visited = [0 for x in range(10000)]
    A, B = map(int, sys.stdin.readline().split())  # 여기서 BFS 돌려봐야 할듯? visited 를 사용하는게 좋을까?
    visited[A] = True

    cur = A
    path = ''
    BFS = collections.deque()
    BFS.append([cur, path])

    while cur != B:
        cur, path = BFS.popleft()

        d = D(cur); s = S(cur); l = L(cur); r = R(cur)
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
    print(path)





