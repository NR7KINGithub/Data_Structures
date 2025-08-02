def countAndSay(n: int) -> str:
    result = "A"

    for _ in range(1, n):
        next_result = ""
        count = 1
    
        for i in range(1, len(result)):
            if result[i] == result[i - 1]:
                count += 1
            else:
                next_result += str(count) + result[i - 1]
                count = 1
    
        next_result += str(count) + result[-1]
        result = next_result
    return result

if __name__ == "__main__":
    print(countAndSay(4))