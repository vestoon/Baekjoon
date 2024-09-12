import sys

# time = [0 for x in range(2**31)]  #
time = []
conferences = {}
count = 0
N = int(sys.stdin.readline())
for g in range(N):
    conf = tuple(map(int, sys.stdin.readline().split()))
    l = conf[1] - conf[0]
    conferences[l] = conferences.get(l, []) + [conf]

# print(conferences)  #

for key in sorted(conferences.keys()):
    # print("key: ", key)  #
    for conf in conferences[key]:
        for t in time:
            if max(t[0], conf[0]) + 1 <= min(t[1], conf[1]):
                break
        else:
            count += 1
            time.append(conf)
            # print(time)  #

print(count)
