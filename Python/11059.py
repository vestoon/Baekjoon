S = list(map(int, input()))
L = len(S)
ans = 0

# 0 1 2 3

for i in range(L-1):
    l, r = S[i], S[i+1] # 0 1
    if l == r:
        ans = max(ans, 2)

    # i ~ j 까지 
    for j in range(i+3, L, 2):
        l += S[(i+j)//2]
        r -= S[(i+j)//2]
        r += S[j] + S[j-1]
        if l == r:
            ans = max(ans, j-i+1)

print(ans)