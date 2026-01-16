import sys
input = sys.stdin.readline

N = int(input())
student_nums = []
for _ in range(N):
  student_nums.append(input().rstrip())

L = len(student_nums[0])
for l in range(1, L+1):
  # 길이가 l 일때 가능한지 탐색
  student_hash = set()
  for st_num in student_nums:
    if st_num[-l:] in student_hash:
      # 중복 발생
      break
    student_hash.add(st_num[-l:])
  else:
    # 중복 없음, 성공
    print(l)
    break
