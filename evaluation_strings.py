def Evaluation(string):
    def check(string):

        return len(string) % 2 == 1

    if check(string):
        tmp = int(string[0])
        for i in range(1, len(string), 2):
            if string[i] == 'A':
                tmp = tmp & int(string[i + 1])

            if string[i] == 'B':
                tmp = tmp | int(string[i + 1])

            if string[i] == 'C':
                tmp = tmp ^ int(string[i + 1])

        return tmp
    return -1



print(Evaluation("1A10"))



