import sys
input = sys.stdin.readline

N = int(input())
refs = list(map(int, input().split()))
refs.sort(reverse=True)

for k in range(N, -1, -1):
    # 인덱싱은 k-1로 해야 함
    # k번째로 큰 논문이 k보다 커야 함
    if k <= refs[k-1]:
        print(k)
        break