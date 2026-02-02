import sys
input = sys.stdin.readline

N = int(input())
study_records = []
boj_records = []
for _ in range(N):
  record = input().rstrip()
  if record[:7] == "boj.kr/":
    boj_records.append(int(record[7:]))
  else:
    study_records.append((len(record), record))
  
study_records.sort()
boj_records.sort()
for l, record in study_records:
  print(record)
for record in boj_records:
  print("boj.kr/", record, sep='')