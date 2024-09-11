import sys
N = int(sys.stdin.readline())
poped = [False for x in range(N + 1)] # 그냥 앞에 0 추가해서 인덱스 똑같이 맞춤
ans = []
pre = 0

for x in range(N):
    flag = False
    new = int( sys.stdin.readline() )
    # print( 'new ', new)
    if new > pre:
        for i in range(pre+1,new+1):
            if not poped[i]:
                ans.append('+')
        ans.append('-')
    else:
        for i in range(pre-1,new,-1):
            if not poped[i]:
                print('NO')
                flag = True
                break
        else:
            ans.append('-')
        if flag:
            break
    poped[new] = True
    # print(ans)
    # print(pre)
    pre = new
    # print(pre)
else:
    for x in ans:
        print(x)
