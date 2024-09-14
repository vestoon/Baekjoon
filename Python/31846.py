import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1; r -= 1

    Mscore = 0
    for joint in range(l, r):  # joint 와 joint+1 사이를 접었을 때
        #점수 계산
        curScore = 0
        for i in range(l, joint+1):
            # s[i] 하고 s[2*j - i + 1] 를 비교해야 함
            if r < 2*joint - i+1:
                continue
            elif S[i] == S[2*joint -i+1]:
                curScore += 1
        
        Mscore = max(Mscore, curScore)
    
    print(Mscore)

