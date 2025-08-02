def productOfDigits(n: int) -> int:
    result = 1
    while n > 0:
        result = result * (n % 10)
        n //= 10
    return result

if __name__ == "__main__":
    n = 5244
    print(productOfDigits(n))