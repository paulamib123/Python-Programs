import math


def is_prime(num):
    if num <= 1:
        return False
    elif num in {2, 3, 5, 7}:
        return True
    elif num % 3 == 0 or num % 2 == 0:
        return False
    else:
        r = 5
        while r * r <= num:
            if num % r == 0:
                return False
            r += 2
            if num % r == 0:
                return False
            r += 4
        return True


def kempner(n):
    i = 1
    if is_prime(n):
        return n
    while i > 0:
        fact = math.factorial(i)
        if fact % n == 0:
            return i
        i += 1


print(kempner(13))
print(kempner(6))
print(kempner(10))
