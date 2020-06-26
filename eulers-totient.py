from math import gcd
from sys import argv

def eulers_totient(num):
    results = [i for i in range(1, num + 1) if gcd(i, num) == 1]
    return results

print(eulers_totient(int(argv[1])))

