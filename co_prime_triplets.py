import math

def pythagorean_triplet():
    list1 = list()
    new_sets = list()
    for b in range(100):
        for a in range(1, b):
            c = math.sqrt(a * a + b * b)
            if c % 1 == 0 and c < 100:
                list1.append([a, b, int(c)])

    for i in range(len(list1)):
        p = list1[i][0]
        q = list1[i][1]
        r = list1[i][2]
        if math.gcd(math.gcd(p, q), r) == 1:
            new_sets.append([p, q, r])
    return new_sets




print(pythagorean_triplet())