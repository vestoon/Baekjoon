N, K = map(int, input().split())
circle = [x for x in range(1, N+1)]
ans = []  # 써클에서 빼서 ans에 추가하기

r = 0  # 반복문 다돌고 끝에 남은 나머지값
while len(circle) > 0:
    n = len(circle)
    # for in range(K-r-1, n, K):
    for i in range(K-r-n-1, 0, K):  # K 씩 증가하는 반복(pop 할때마다 리스트의 길이가 줄기 때문에 뒤에서부터 센다)
        # print(i)
        ans.append(circle.pop(i))
    r = (n - (K-r)) % K  # 반복 끝나고 남은 값 정의
    # print('n =', n, 'r =', r)
print('<', end='')
for a in ans[:-1]:
    print(a, end=', ')
print(ans[-1], end='')
print('>')
