def is_palindrome_possible(s: str) -> bool:
    count_alpha = {}
    for ch in s:
        count_alpha[ch] = s.count(ch)

    if s == s[::-1]:
        return True
    if all(value == 2 for value in count_alpha.values()):
        return True
    if sum(value for value in count_alpha.values()) == len(count_alpha) * 2 - 1:
        return True
    return False
