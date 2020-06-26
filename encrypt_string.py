string = "hello"
def encrypt(string, key):
    z = []
    for i in range(len(string)):
        if string.count(string[i]) % 2 == 0:
            if ord(string[i]) + key >= 122:
                z.append(chr(ord(string[i]) + key - 26))
            else:
                z.append(chr(ord(string[i]) + key))

        elif string.count(string[i]) % 2 == 1:
            if ord(string[i]) - key <= 65:
                z.append(chr(ord(string[i]) - key + 26))
            else:
                z.append(chr(ord(string[i]) - key))

    return "".join(z)


print(encrypt(string, 3))
