import math


def fact(n: int) -> int:
    return len(str(math.factorial(n))) - len(str(math.factorial(n)).strip('0'))





