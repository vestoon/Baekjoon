import sys

T = int(sys.stdin.readline())
for g1 in range(T):
    M, N, K = map(int, sys.stdin.readline().split())  # 가로가 M, 세로가 N
    # farm = [[0 for x in range(M)] for x in range(N)]  # 배추밭 만들기

    cabbages = []
    for g2 in range(K):  # 배추 좌표 저장하기
        j, i = map(int, sys.stdin.readline().split())  # i행 j열
        cabbages.append((i, j))
    # print('cabbages:', cabbages)

    earthworms = []
    group = set()  # earthworm 에 추가하기 전에 임시로 넣어두는 곳
    while cabbages:  #
        # print('cabbages in while:', cabbages)
        for cabbage in cabbages:
            # print('cabbage:', cabbage)
            if not group:
                group = {cabbage}
                cabbages.remove(cabbage)  # group 에 넣었기 때문에 cabbages 에서 삭제
                break  # 이렇게 찾을 때마다 break 를 걸고 다시 앞으로 돌아가는건 너무 비효율적인데... else를 사용하기 위한 플래그를 하나 만들어야 하나...
            else:
                i = cabbage[0]
                j = cabbage[1]
                # print('now group:', group)
                flag = 0
                for near in {(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)}:  # 선택한 배추의 인접 배추들
                    # print('near:', near)
                    if near in group:
                        # print('find!')
                        group.add(cabbage)
                        cabbages.remove(cabbage)  # group 에 넣었기 때문에 cabbages 에서 삭제
                        flag = 1  # 이중 break 를 위한 플래그
                        break  # 이중 break
                if flag:
                    break
        else:
            # print('group:', group)
            earthworms.append(group)
            group = set()
    if group:  # 제일 마지막 그룹이 완성되면 반복문이 실행되지 않으므로 직접 추가
        earthworms.append(group)
    print(len(earthworms))
