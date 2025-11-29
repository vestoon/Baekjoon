import sys
input = sys.stdin.readline

N, J, S, H, K = map(int, input().split())
stage = []
for _ in range(3):
	stage.append(input().rstrip())

# 장애물 종류
jmp1, jmp2, slide = 0, 0, 0
for j in range(N):
	if stage[0][j] == 'v':
		slide += 1
	elif stage[1][j] == '^':
		jmp2 += 1
	elif stage[2][j] == '^':
		jmp1 += 1

# 상단 장애물 계산
H -= K*max(0, slide - S)
# 낮은 장애물부터 우선적으로 통과
if jmp1 < J:
	# 낮은 장애물을 전부 통과할 수 있는 경우
	J -= jmp1

	# 높은 장애물 계산
	jmp2 *= 2
	jmp2 -= J
	if 0 < jmp2:
		H -= K*(jmp2//2 + jmp2%2)
else:
	# 낮은 장애물도 다 통과할 수 없는 경우
	jmp1 -= J
	H -= K*(jmp1 + jmp2)

print(H if 0 < H else -1)


