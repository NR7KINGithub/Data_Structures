def checkPalindromString(s: str) -> bool:
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        
        i += 1
        j -= 1
        
    return True

if __name__ == "__main__":
    s = "madam"
    print(checkPalindromString(s))