def odd(n: int) -> bool:
    return n % 2 == 1


def is_feasible(loaves_held: [int]):
    return not odd(convert(loaves_held).count('O'))


def oddeven(loaves: int) ->str:
    return 'O' if loaves % 2 == 1 else 'E'


def convert(loaves_held: [int]) -> str:
    return ''.join([oddeven(n) for n in loaves_held])


def loaves_needed(oe: str) -> int:
    return sum([2*len(x) + 2 for x in oe.split('O')[1::2]])


def fair_rations(loaves: [int]) -> int:
    if not is_feasible(loaves):
        return -1
    else:
        return loaves_needed(convert(loaves))


ar = [2,1]

print(fair_rations(ar))


