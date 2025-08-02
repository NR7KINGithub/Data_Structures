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

"""//Java Solution
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int left = 0, longest = 0;
        Set<Character> set = new HashSet<>();
        for (int right = 0; right < n; right++) {
            while (set.contains(s.charAt(right))) {
                set.remove(s.charAt(left));
                left++;
            }
        set.add(s.charAt(right));
        longest = Math.max(longest, right - left + 1); 
    }
    return longest;
    }
}"""