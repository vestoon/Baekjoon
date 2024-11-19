import sys
input = sys.stdin.readline

"""
모든 경우 완탐 돌리기
H < J < S
H < S < J
J < H < S
J < S < H
S < J < H
S < H < J

"""
N = int(input())
 
inp1, inp2, inp3 = input().rstrip(), input().rstrip(), input().rstrip()


def compare2(a, b, order): # a < b 인지 판별
    for j in range(N):
        if order[a[j]] < order[b[j]]:
            return True
        if order[a[j]] > order[b[j]]:
            return False
    return False

def compare3(a, b, c, order):
    if compare2(a, b, order) and compare2(b, c, order):
        return True
    return False

if compare3(inp1, inp2, inp3, {'H':1, 'J':2, 'S':3}):
    print("HJS! HJS! HJS!")
elif compare3(inp1, inp2, inp3, {'H':1, 'J':3, 'S':2}):
    print("HJS! HJS! HJS!")
elif compare3(inp1, inp2, inp3, {'H':2, 'J':1, 'S':3}):
    print("HJS! HJS! HJS!")
elif compare3(inp1, inp2, inp3, {'H':2, 'J':3, 'S':1}):
    print("HJS! HJS! HJS!")
elif compare3(inp1, inp2, inp3, {'H':3, 'J':1, 'S':2}):
    print("HJS! HJS! HJS!")
elif compare3(inp1, inp2, inp3, {'H':3, 'J':2, 'S':1}):
    print("HJS! HJS! HJS!")
else:
    print("Hmm...")
