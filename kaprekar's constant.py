def smallest(n: int) -> int:
    return int("".join(sorted(str(n))))


def largest(n: int) -> int:
    return int("".join(sorted(str(n))[::-1]))


def difference(n: int) -> int:
    return largest(n) - smallest(n)


def kaprekar(n: int) -> int:

    if difference(n) == 6174:
        return 6147
    else:
        kaprekar(difference(n))


print(kaprekar(5374))




