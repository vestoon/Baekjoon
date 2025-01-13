import sys
input = sys.stdin.readline

"""
주어진 방식으로 암호화가 가능한지 확인하는 문제 
순서를 자유롭게 바꿀 수 있기 때문에 특정 문자열이 몇 개 들어갔느지를 확인해야 한다. 
문자열 길이가 10만개기 때문에 완탐은 힘들 듯
암호화된 문자열 중간에 원래 문자열을 찾으면 되는데 아마도 한 칸씩 옮겨 가면서 +-1 방식으로 탐색해야 할듯?
문자열 인덱스가 26가지 있는 리스트로 만들면 될 것 같은데 일치하는지는 어떻게 확인하지?
일치하는 문자열 개수를 셀까?
"""

T = int(input())
for _ in range(T):
    encoded = input().rstrip()
    origin = input().rstrip()
    l = len(origin)
    cnt_correct = 0
    
    origin_cnt = [0 for x in range(26)]
    cur_cnt = [0 for x in range(26)]
    for s in origin:
        origin_cnt[ord(s)-97] += 1

    for i in range(l):
        s = encoded[i]
        cur_cnt[ord(s)-97] += 1
        if cur_cnt[ord(s)-97] <= origin_cnt[ord(s)-97]:
            cnt_correct += 1
    
    i, j = 0, l-1
    while True:
        if cnt_correct == l:
            print("YES")
            break
        
        if cur_cnt[ord(encoded[i])-97] <= origin_cnt[ord(encoded[i])-97]:
            cnt_correct -= 1
        cur_cnt[ord(encoded[i])-97] -= 1
        i += 1


        j += 1
        if j == len(encoded):
            print("NO")
            break
        cur_cnt[ord(encoded[j])-97] += 1
        if cur_cnt[ord(encoded[j])-97] <= origin_cnt[ord(encoded[j])-97]:
            cnt_correct += 1
        


    
    
