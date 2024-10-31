import sys
input = sys.stdin.readline

N = int(input())
left, right = input().split('*')
right = right.rstrip()


for _ in range(N):
    fileName = input().rstrip()
    if len(fileName) < len(left) + len(right):
        print("NE")
        continue
    if fileName[:len(left)] == left and fileName[-len(right):] == right:
        print("DA")
    else:
        print("NE")

