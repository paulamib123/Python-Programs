def fair_rations(b:[int]) -> int:
    cnt = 0
    for i in range(len(b) - 1):
        if b[i] % 2 == 1:
            b[i] += 1
            b[i + 1] += 1
            cnt += 2
    if b[-1] % 2 == 1:
        return -1
    else:
        return cnt


print(fair_rations([2, 3, 4, 5, 6, 8, 7, 9]))
