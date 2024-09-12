N = int(input())

adj_list = {}
for _ in range(N):
    root, l, r = input().split()
    adj_list[root] = [l, r]

pre_order = []
in_order = []
post_order = []
visited = [False for x in range(26)]


def dfs(p):
    visited[ord(p)-65] = True
    pre_order.append(p)

    left = adj_list[p][0]
    right = adj_list[p][1]

    if left != '.' and not visited[ord(left)-65]:
        dfs(left)
    in_order.append(p)
    if right != '.' and not visited[ord(right)-65]:
        dfs(right)

    visited[ord(p)-65] = False
    post_order.append(p)


dfs('A')
for x in pre_order:
    print(x, end='')
print()

for x in in_order:
    print(x, end='')
print()

for x in post_order:
    print(x, end='')
print()

