H100 = " Hundred"


def convert2digits(n: int) -> str:
    upto20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    if n < len(upto20):
        return upto20[n]
    return tens[n // 10] + " " + upto20[n % 10]


def convert3digits(n: int) -> str:
    if n < 100:
        return convert2digits(n)
    return fix_and(convert2digits(n // 100) + " " + H100 + " " + convert2digits(n % 100))


def fix_and(s: str) -> str:
    if H100 in s and not s.endswith(H100):
        return s.replace(H100, H100 + " and ")
    else:
        return s


W_DENOMS = [10 ** 9, 10 ** 6, 1000, 1]
I_DENOMS = [10 ** 7, 10 ** 5, 1000, 1]

W_DENOM_NAMES = ["Billion", "Million", "Thousand", ""]
I_DENOM_NAMES = ["Crore", "Lakh", "Thousand", ""]

Ws = dict(zip(W_DENOMS, W_DENOM_NAMES))
Is = dict(zip(I_DENOMS, I_DENOM_NAMES))


def split_into_denoms(amount: int, denoms: [int]) -> [(int, int)]:
    if len(denoms) == 1:
        return[(denoms[0], amount)]
    else:
        return [(denoms[0], amount // denoms[0])] + split_into_denoms(amount % denoms[0], denoms[1:])


def convert_denoms(splits: [(int, int)], names: {int: str}) -> [(str, int)]:
    return [(names[x[0]], x[1]) for x in splits]


def convert_multiples(splits:[(str, int)]) -> [(str, str)]:
    return [(convert3digits(x[1]), x[0]) for x in splits]


def combine(pieces: [(str, str)]) -> [str]:
    return ["".join(x + y) for x, y in pieces if len(x.strip()) != 0]


step1 = split_into_denoms(123456789, W_DENOMS)
print(step1)
step2 = convert_denoms(step1, Ws)
print(step2)
step3 = convert_multiples(step2)
print(step3)
step4 = ' '.join(combine(step3))
print(step4.capitalize())






