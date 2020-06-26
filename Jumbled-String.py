def pick10(s: str, start: int, STEPS: int) -> str:
    steps = [(n * (n + 1)) // 2 for n in range(STEPS)]
    print(steps)
    stops = [(start + step) % len(s) for step in steps]
    print(stops)
    return "".join([s[stop] for stop in stops])


print(pick10("ABC", 1, 10))
