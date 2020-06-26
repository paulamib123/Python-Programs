def digital_no(n):
    n = str(n)
    total = 0
    for i in range(len(n)):
        total = (total + int(n[i])) % 9

    if total == 0:
        return 9
    else:
        return total


print(digital_no(65785412))
print(digital_no(45893))