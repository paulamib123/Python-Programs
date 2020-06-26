def expand(num):
    ans = []

    for position, digit in enumerate(str(num)[::-1]):
        if int(digit) != 0:
            ans.append(digit + ('0' * position))

    return ' + '.join(ans[::-1])


print(expand(86))
print(expand(13))
print(expand(5325))
