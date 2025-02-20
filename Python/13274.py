import sys
input = sys.stdin.readline

# 그냥 깡 구현....?
def main(): 
    N, K = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    
    for _ in range(K):
        # 오름차순 정렬 후 A[L-1] ~ A[R-1] 까지 X 를 더하고 다시 정렬
        L, R, X = map(int, input().split())
        for i in range(L-1, R):
            A[i] += X
        A.sort()
            
            
    print(*A)

main()