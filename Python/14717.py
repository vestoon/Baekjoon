import sys
input = sys.stdin.readline

A, B = map(int, input().split())

"""
전체 경우의 수: 18C2 = 153

리스트 순회하면서 경우의 수 계산하고 확률로 바꾸자

"""

def score(a:int, b:int) -> int:
    if a == b:
        return 10+a
    return (a+b)%10 + 1

cnt = [2 for x in range(11)]
cnt[A] -= 1; cnt[B] -= 1
deck = []

for i in range(1, 11):
    for _ in range(cnt[i]):
        deck.append(i)

# print(deck)
myScore = score(A, B)
# print(myScore)
prob = 0
for i in range(18):
    for j in range(i+1, 18):
        if score(deck[i], deck[j]) < myScore:
            prob += 1

print(format(prob/153, ".3f"))

