E, EM, M, MH, H = map(int, input().split())
ans = 0

while True:
    if E:
        E -= 1
    elif EM:
        EM -= 1
    else:
        break

    if H:
        H -= 1
    elif MH:
        MH -= 1
    else:
        break

    if M:
        M -= 1
    elif not EM and not MH:
        break
    elif EM > MH:
        EM -= 1
    elif MH >= EM:
        MH -= 1

    ans += 1

print(ans)

