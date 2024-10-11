import sys
input = sys.stdin.readline

def getFriendNum(n: int) -> int:
    ret = 0
    while n:
        r = n%10
        ret |= 1 << r
        n //= 10
    
    return ret


def isAlmostFriend(x:int, y:int) -> bool:
    strX , strY= str(x), str(y)
    
    for i in range(len(strX)-1):
        # (+1, -1)
        if strX[i] != '9' and strX[i+1] != '0':
            tmp = strX[:i] + str(int(strX[i])+1) + str(int(strX[i+1])-1) + strX[i+2:]
            if getFriendNum(int(tmp)) == getFriendNum(y):
                return True

        # (-1, +1)
        if not (i == 0 and strX[i] == '1') and strX[i] != '0' and strX[i+1] != '9':
            tmp = strX[:i] + str(int(strX[i])-1) + str(int(strX[i+1])+1) + strX[i+2:]
            if getFriendNum(int(tmp)) == getFriendNum(y):
                return True
    
    for j in range((len(strY)) - 1):
        #(+1, -1)
        if  strY[j] != '9' and strY[j+1] != '0':
            tmp = strY[:j] + str(int(strY[j])+1) + str(int(strY[j+1])-1) + strY[j+2:]
            # print('tmp', tmp)
            if getFriendNum(int(tmp)) == getFriendNum(x):
                return True
        
        #(-1, +1)
        if not (j == 0 and strY[j] != '1') and strY[j] != '0' and strY[j+1] != '9':
            tmp = strY[:j] + str(int(strY[j])-1) + str(int(strY[j+1])+1) + strY[j+2:]
            if getFriendNum(int(tmp)) == getFriendNum(x):
                return True
    
    return False


for _ in range(3):
    x, y = map(int, input().split())
    if getFriendNum(x) == getFriendNum(y):
        print("friends")
        continue

    if isAlmostFriend(x, y):
        print("almost friends")
    else:
        print("nothing")


