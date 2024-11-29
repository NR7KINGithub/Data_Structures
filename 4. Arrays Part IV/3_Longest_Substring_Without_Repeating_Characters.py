def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    longest = 0
    sett = set()
    n = len(s)
    
    for right in range(n):
        while s[right] in sett:
            sett.remove(s[left])
            left += 1
            
        length = (right-left)+1
        longest = max(longest, length)
        sett.add(s[right])
        
    return longest

if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))