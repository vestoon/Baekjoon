import sys
input = sys.stdin.readline

def sol() -> int:
    N = int(input())

    pointer = [-1 for x in range(N+1)] # pointer[i] : i번 사람이 가리키고 있는 사람 번호
    visited  = [False for x in range(N+1)]
    for n in range(1, N+1):
        A = int(input())
        pointer[n] = A
    
    ret = 0
    cur = 1
    visited[1] = True
    while True:
        cur = pointer[cur] # 위치 이동
        ret += 1 # 이동 횃수 증가
        if cur == N: # 찾았다면 return
            return ret
        if visited[cur]: # 이미 방문한 곳이라면 사이클이 생기기 때문에 0
            return 0
        visited[cur] = True


T = int(input())
for tc in range(1,T+1):
    print(sol())


