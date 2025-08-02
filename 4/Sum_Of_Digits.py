def sumOfDigits(n: int, r: int) -> int:
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10

    product = sum * r

    result = 0
    while product > 0:
        result += product % 10
        product //= 10

    return result

if __name__ == "__main__":
    n = 99
    r = 3
    print(sumOfDigits(n, r))