import sys
input = sys.stdin.readline

N = int(input())
myCards = list(map(int, input().split()))
yourCards = list(map(int, input().split()))

myCards.sort()
yourCards.sort()

i = 0
cnt = 0
win = False

for card in myCards:

    while i < N:
        if card < yourCards[i]:
            cnt += 1
            i += 1
            break
        i += 1
    
    if cnt >= (N+1)//2:
        win = True
        break
else:
    win = False

print("YES" if win else " NO")
