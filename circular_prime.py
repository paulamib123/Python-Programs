def circular_rotation(n):
    def rotations(n):
        n = str(n)
        l = []
        for i in range(len(n)):
            l.append(int(n[1:] + n[0]))
        return l

    def prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    for j in rotations(n):
        if not prime(j):
            return False
        return True











