import sys

idx = 0 # 현재 순열의 순서
no_permutation = "No permutation"

def sol(arr:list[str], offset:int, tar_i):
  global idx
  # base case
  if offset == len(arr) - 1: 
    idx += 1
    return ''.join(arr) if idx == tar_i else no_permutation

  for i in range(offset, len(arr)):
    arr[offset], arr[i] = arr[i], arr[offset]

    ret = sol(arr, offset+1, tar_i)
    if ret != no_permutation:
      return ret
  
  # arr 원상 복구
  arr[offset:] = arr[offset+1:] + arr[offset:offset+1]
  return no_permutation

for inp in sys.stdin:
  idx = 0 # 전역 변수 초기화
  arr, tar_i = inp.split()
  arr = list(arr)
  tar_i = int(tar_i)
  print(''.join(arr), tar_i, '=', sol(arr, 0, tar_i))
