def makeMaxPrice(coupon:str):
  for i in range(len(coupon)):
    coupon[i] = coupon[i] if coupon[i] != '?' else '9'
  return ''.join(coupon)

def sol():
  N, coupon = input().split()
  N = int(N)
  # 전부 문자열로 통일해서 저장
  coupon = list(coupon)
  A = list(input()) 

  # 아무 수나 상관 없으니까 그냥 전부 9로 채우기
  maxPrice = makeMaxPrice(coupon)

  # 자릿수로 먼저 비교
  if len(A) < len(coupon):
    print(makeMaxPrice(coupon))
    return

  if len(coupon) < len(A):
    print(-1)
    return
  
  # 자릿수 같을 때
  for i in range(N):
    a, c = A[i], coupon[i]
    if c == '?':
      if a != '9':
        print(maxPrice)
        return
    else: # c != '?'
      if int(c) < int(a):
        print(-1)
        return
      if int(a) < int(c):
        print(maxPrice)
        return
  
  print(maxPrice)
  return

sol()