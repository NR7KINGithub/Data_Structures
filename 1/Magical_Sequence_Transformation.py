def solve(s: str) -> int:
    stack = []
    power = 0
    
    for ch in s:
        if stack and ((stack[-1] == 'X' and ch == 'Y') or (stack[-1] == 'Y' and ch == 'X')):
            stack.pop()
            power += 1

        else:
            stack.append(ch)

    return power

def main():
    import sys
    s = "XXYYYXXYXYXYXYXXYXYXXXYXYXYXXYYYYYYXXX"
    result = solve(s)
    print(result)

if __name__ == "__main__":
    main()