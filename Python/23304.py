def isAkaraka(target) :
    if len(target) == 1:
        return True
    
    l = len(target)
    h = l//2
    for i in range(h):
        if target[i] != target[l-1 - i]:
            return False
    
    if isAkaraka(target[:h]):
        return True



S = input().rstrip()
# if isAkaraka(S):
#     print("AKARAKA")
# else:
#     print("IPSELENTI")

print("AKARAKA" if isAkaraka(S) else "IPSELENTI")