import sys
input = sys.stdin.readline

N = int(input())
data = {"ChongChong": True}
cnt = 1

for _ in range(N):
    A, B = input().split()
    data[A] = data.get(A, False)
    data[B] = data.get(B, False)

    if data[A] and not data[B]:
        data[B] = True
        cnt += 1
    elif data[B] and not data[A]:
        data[A] = True
        cnt += 1

print(cnt)


