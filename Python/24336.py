#  https://www.acmicpc.net/problem/24336
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

def totalTime(s):
    h = int(s[:2])
    m = int(s[3:])

    return h*60 + m

M = 24*60 # 하루가 총 몇 분인지
dist = {
    "Seoul": 0.0,
    "Yeongdeungpo": 9.1,
    "Anyang": 23.9,
    "Suwon": 41.5,
    "Osan": 56.5,
    "Seojeongri": 66.5,
    "Pyeongtaek": 75.0,
    "Seonghwan": 84.4,
    "Cheonan": 96.6,
    "Sojeongni": 107.4,
    "Jeonui": 114.9,
    "Jochiwon": 129.3,
    "Bugang": 139.8,
    "Sintanjin": 151.9,
    "Daejeon": 166.3,
    "Okcheon": 182.5,
    "Iwon": 190.8,
    "Jitan": 196.4,
    "Simcheon": 200.8,
    "Gakgye": 204.6,
    "Yeongdong": 211.6,
    "Hwanggan": 226.2,
    "Chupungnyeong": 234.7,
    "Gimcheon": 253.8,
    "Gumi": 276.7,
    "Sagok": 281.3,
    "Yangmok": 289.5,
    "Waegwan": 296.0,
    "Sindong": 305.9,
    "Daegu": 323.1,
    "Dongdaegu": 326.3,
    "Gyeongsan": 338.6,
    "Namseonghyeon": 353.1,
    "Cheongdo": 361.8,
    "Sangdong": 372.2,
    "Miryang": 381.6,
    "Samnangjin": 394.1,
    "Wondong": 403.2,
    "Mulgeum": 412.4,
    "Hwamyeong": 421.8,
    "Gupo": 425.2,
    "Sasang": 430.3,
    "Busan": 441.7,
}


ioHistory = []  # (장소, 출발, 도착)

station, arrive, leave = input().split()
ioHistory.append((station, 0, leave))
for i in range(N-2):
    station, arrive, leave = input().split()
    ioHistory.append((station, arrive, leave))
station, arrive, leave = input().split()
ioHistory.append((station, arrive, 0))

for _ in range(Q):
    satation1, station2 = input().split()

    time = 0
    i = 0
    while ioHistory[i][0] != satation1:
        i += 1
    
    # time += (totalTime(ioHistory[i+1][1]) - totalTime(ioHistory[i][2]))
    # i += 1
    # while ioHistory[i][0] != station2:
    #     time += (totalTime(ioHistory[i][2]) - totalTime(ioHistory[i][1])) % M
    #     time += (totalTime(ioHistory[i+1][1]) - totalTime(ioHistory[i][2])) % M
    #     i += 1
    # # 상행, 하행이냐에 따라서 가는 방향이 다르다!
    
    # distance = abs(dist[satation1] - dist[station2])
    # print(distance)
    # print(time)
    # print((distance/time)*60)


    j = i
    while ioHistory[j][0] != station2:
        j += 1
    
    time = (totalTime(ioHistory[j][1]) - totalTime(ioHistory[i][2])) % M
    # print(time)
    distance = abs(dist[satation1] - dist[station2])
    # print(distance)
    print((distance/time)*60)
