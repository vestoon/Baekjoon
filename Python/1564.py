N = int(input())

"""
N 팩토리얼의 끝의 5자리를 구하는 문제 

끝의 5자리만 구하려면 100000로만 나눠주면 되지만 끝의 0을 제거하는게 문제가 된다
한번 곱할 때마다 뒤에 0이 추가될 경우를 생각해서 나누는 수(저장하는 자릿수)를 여유 있게 잡아야 한다. 
그렇다면 얼마나 여유 있게 잡아야 하냐는 것이 시간을 결정하는 중요한 요소가 된다. 

5에다가 추가로 저장하는 자릿수를 k라고 하고
지금까지 저장해온 값이 num, 앞으로 곱해가는 값이 i라고 하자 

자릿수에 추가되는 0은 2와 5의 곱으로 이루어져 있다.
즉, num에 i를 곱할 때 얼마나 많은 2와 5가 결합하가 자릿수가 증가하는 정도라 할 수 있다.

i의 경우는 최대 1,000,000 까지이다 
2의 경우 2^19 = 524288 까지이고
5의 경우는 5^8 = 390625 까지 넣을 수 있다. 

num이 소인수로 2^8 이상을 가지고 있다면 곱할 때 뒤에 0이 8자리까지 붙을 수 있기 때문에 k는 8이다. 
그렇다면 2^19로 뒤에 0이 19개가 붙는 경우도 있지 않을까?

일단 결론을 말하자면 num은 소인수로 5를 가질 수 없기 때문이고 이는 5가 2보다 크기 때문이다. 
우리는 num 에 i를 곱할 때마다 k+5 자리만 저장하기 때문에 mod 10^13 연산을 취할 것이고 따라서 정확한 소인수를 계산할 수는 없지만
하지만 우리는 num에 i를 곱한 후에는 항상 뒤의 10을 제거한다.
2<5 이기 때문에 1~5 까지 곱하다 보면 항상 5가 부족하고 5의 배수는 항상 1의 자리가 0혹은 5이기 때문에 이는 mod 연산을 취해도 달라지지 않는다.

따라서 num *= i 를  할 때에 증가하는 0의 수는 오로지 i의 소인수 중 5의 지수에 따라서 결정된다
k = 8 이다.

|12345000000|
"""
mod = 10**13
num = 1

for i in range(2, N+1):
    num = (num*i) % mod
    
    while num%10 == 0:
        num //= 10

print(str(num)[-5:].zfill(5))

# print(2**19)
# print(5**9)
