def total(n: int) -> int:
    return sum([int(x)**len(str(n)) for x in str(n)])


def is_armstrong(n: int) -> bool:
    return total(n) == n


def armstrong_in_range(start: int, end: int) -> [int]:
    l1 = []
    for i in range(start, end+1):
        if is_armstrong(i):
            l1.append(i)
    return l1
