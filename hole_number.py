def holes(limit):

    def digits(n):
        return [ch for ch in str(n)]

    count = {'0': 1, '4': 1, '6': 1, '8': 2, '9': 1}
    sums = 0
    for i in range(1, limit+1):
        for num in digits(i):
            if num in count:
                return sum(count[num])









print(holes(14))