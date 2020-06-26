def isDoubleBasePalindrome(n):
    def isbinary(n):
        z = bin(n).replace("0b", "")
        return str(z) == str(z)[::-1]

    def palindrome(n):
        return str(n) == str(n)[::-1]

    return isbinary(n) and palindrome(n)