import sys
N = int(sys.stdin.readline())
video = []

for g in range(N):
    line = tuple(sys.stdin.readline().rstrip())
    video.append(line)


def quad(v):
    # print(v)  #
    ret = ''
    start = v[0][0]
    for i in v:
        for j in i:
            if j != start:
                ret += '('
                l = int(len(v) / 2)
                for row in range(0, len(v), l):
                    for col in range(0, len(v), l):
                        quadV = [x[col:col+l] for x in v[row:row+l]]
                        ret += quad(quadV)
                ret += ')'
                break
        else:
            continue
        break
    else:
        ret += start

    return ret


print(quad(video))
