import sys
T = int(sys.stdin.readline())
for test_case in range(T):
    n = int(sys.stdin.readline())
    closet = {}
    for x in range(n):
        name, cloth_type = sys.stdin.readline().split()
        cloth_type = cloth_type.rstrip()
        closet[cloth_type] = closet.get(cloth_type, 0) + 1

    ans = 1
    for item in closet.items():
        ans *= item[1] + 1
    print(ans-1)

