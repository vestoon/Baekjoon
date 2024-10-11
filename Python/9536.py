import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    data = {}
    total = input().split()

    while True:
        info = input().rstrip()
        if info == "what does the fox say?":
            break 
    
        key, _, value = info.split()
        data[value] = key

    for voice in total:
        if voice in data:
            continue
        else:
            print(voice, end='')
            print()