X, Y = map(int, input().split())


"""
X = a^2 + b^2 + c^2 + d^2
Y = a^2 + b^2 + c^2 + d^2 + 2ab + 2cd

Y > X 여야 함

"""

M = (2*X - Y)*506

if X > Y:
    print(-1)
else:
    print(M if M >= 0 else -1)  

