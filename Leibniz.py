def sign_change(sign: int) -> int:
    return sign * -1


def leibniz_sum(n: int) -> int:
    sign = 1
    total = 0
    for denominator in range(1, 2*n, 2):
        total += sign * (1/denominator)
        sign = sign_change(sign)
    return total

