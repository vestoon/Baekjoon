import sys
input = sys.stdin.readline

R, C = map(int, input().split())
puzzle = []
ans = 'z'*21

for _ in range(R):
    line = list(input().rstrip())
    puzzle.append(line)


for i in range(R):
    sharp = [-1] # '#' 이 있는 인덱스
    for j in range(C):
        if puzzle[i][j] == '#':
            sharp.append(j)
    sharp.append(C)

    for k in range(len(sharp)-1):
        word = puzzle[i][sharp[k]+1:sharp[k+1]] # 아직은 리스트 형태
        word = ''.join(word)
        if len(word) >= 2:
            ans = min(word, ans)

for j in range(C):
    sharp = [-1]
    for i in range(R):
        if puzzle[i][j] == '#':
            sharp.append(i)
    sharp.append(R)

    for k in range(len(sharp)-1):
        word = [puzzle[x][j] for x in range(sharp[k]+1, sharp[k+1])]
        word = ''.join(word)
        if len(word) >= 2:
            ans = min(word, ans)


print(ans)


    
