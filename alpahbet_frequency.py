from sys import argv
from collections import Counter
from string import ascii_uppercase
import matplotlib.pyplot as plt 

def count_frequency(filename):
    with open(filename) as f:
        frequency = Counter(letter for line in f for letter in line.upper() if letter in ascii_uppercase)
    
    frequency = sorted(frequency.items())
    x = [i[0] for i in frequency]
    y = [i[1] for i in frequency]
    
    return x, y


x, y = count_frequency(argv[1])

plt.bar(x, y)
plt.xlabel('Alphabets')
plt.ylabel('Frequency')
plt.title('Frequency of Letters in ' + argv[1])
plt.show()

