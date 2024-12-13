def countAndSay(n: int) -> str:
    # Start with the first term in the sequence
    result = "1"

    # Generate terms from 2 to n
    for _ in range(1, n):
        next_result = ""
        count = 1
    
        # Iterate over the previous result to count consecutive digits
        for i in range(1, len(result)):
            if result[i] == result[i - 1]:
                count += 1 # Increment count if the current digit is the same as the previous one
            else:
                next_result += str(count) + result[i - 1] # Append count and digit to the next term
                count = 1 # Reset the count for the new digit
    
        # Add the last counted group (since the loop ends without appending it)
        next_result += str(count) + result[-1]
        # Update result to the new term
        result = next_result
    return result

if __name__ == "__main__":
    print(countAndSay(4))