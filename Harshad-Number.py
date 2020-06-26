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


def sum_of_digits(n):
    return sum([int(n) for n in str(n)])


def morannumbers(n):
    if n % sum_of_digits(n) == 0 and is_prime(n // sum_of_digits(n)):
        return 'M'
    if n % sum_of_digits(n) == 0:
        return 'H'
    return 'Neither'



