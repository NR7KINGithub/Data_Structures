def longestPalindrome(s: str) -> str:
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the expanded palindrome substring
        return s[left + 1:right]

    if len(s) < 2:
        return s

    longest = ""
    for i in range(len(s)):
        # Odd-length palindromes
        odd_palindrome = expand_around_center(i, i)
        # Even-length palindromes
        even_palindrome = expand_around_center(i, i + 1)
        # Compare and choose the longer palindrome
        longest = max(longest, odd_palindrome, even_palindrome, key=len)

    return longest
    
if __name__ == "__main__":
    print(longestPalindrome("babad"))