def series():
    result = [(25 ** i) % 101 for i in range(1, 101)]
    return result

print(series())
print(sorted(series()))

#Fermants little theorem
#Extended Euclids Algorithm
# (2 ** 3 ** 4 upto100) % 101
# (x ** 28) % 101
