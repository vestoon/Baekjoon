inp = input()
i = 0 # 현재 바라보고 있는 inp의 인덱스
l = len(inp)

cur = 0 # 현재 사용하고 있는 수
while i != l:
    cur += 1
    cur_str = str(cur)
    for j in range(len(cur_str)):
        if inp[i] == cur_str[j]:
            i += 1
            if i == l:
                break

print(cur)