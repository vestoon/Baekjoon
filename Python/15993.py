import sys
import collections
input = sys.stdin.readline
mod = 1000000009

M = 0
T = int(input())
query = []
for tc in range(1, T+1):
    n = int(input())
    M = max(n, M)
    query.append(n)


even_cnt = [0 for x in range(M+1)]
odd_cnt = [0 for x in range(M+1)]

for i in range(1, min(4, M+1)):
    odd_cnt[i] = 1

for i in range(1, M+1):
    if i+1 < M+1:
        odd_cnt[i+1] += even_cnt[i]
        even_cnt[i + 1] += odd_cnt[i]
        odd_cnt[i+1] %= mod
        even_cnt[i+1] %= mod
    if i+2 < M+1:
        odd_cnt[i+2] += even_cnt[i]
        even_cnt[i + 2] += odd_cnt[i]
        odd_cnt[i+2] %= mod
        even_cnt[i+2] %= mod
    if i+3 < M+1:
        odd_cnt[i+3] += even_cnt[i]
        even_cnt[i+3] += odd_cnt[i]
        odd_cnt[i+3] %= mod
        even_cnt[i+3] %= mod

# print(odd_cnt)
# print(even_cnt)
# print()
for q in query:
    print(odd_cnt[q], even_cnt[q])
