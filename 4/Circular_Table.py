def seatingArrangement(n: int) -> int:
    fact = 1
    for i in range(1, n):
        fact *= i

    return 2 * fact


if __name__ == "__main__":
    n = 4
    print(seatingArrangement(n))