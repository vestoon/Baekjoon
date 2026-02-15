import sys

factor = [0 for x in range(11)]
factor[1] = 1
max_l = 1 # 지금까지 기록하고 있는 가장 큰 팩토리얼

for inp in sys.stdin:
  arr, target = inp.split()
  tar_i = int(target) - 1
  l = len(arr)

  # factorial 게산
  if max_l < l:
    for i in range(max_l + 1, l+1):
      factor[i] = factor[i-1]*i
  
  ret = ''
  if tar_i < factor[l]:
    rest = arr
    while len(rest) != 1:
      perm_size = factor[len(rest)-1]
      q = (tar_i)//perm_size

      tar_i -= perm_size*q
      ret += rest[q]
      rest = rest[:q] + rest[q+1:]
    # 마지막 하나 남은 거 추가
    ret += rest
  else:
    ret = "No permutation"
    
  print(arr, target, '=', ret)
