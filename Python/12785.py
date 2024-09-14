# https://www.acmicpc.net/problem/12785
import math

print("??")

INF = 1000007
w, h = map(int, input().split())
x, y = map(int, input().split())

home2toast = math.comb(x-1 + y-1, x-1)
toast2school = math.comb(w-x + h-y, w-x)

print(home2toast*toast2school % INF)
