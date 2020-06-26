def boolean_combo (n: int) -> [bool]:
    return n % 5 == 0, n % 3 == 0


def Fizzbuzz(n: int) -> str:
    return {(False, False): str(n), (True, False): "Buzz", (False, True): "Fizz", (True, True): "FizzBuzz"}[boolean_combo(n)]


