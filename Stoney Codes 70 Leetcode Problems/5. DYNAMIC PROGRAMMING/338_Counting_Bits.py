from typing import List

def countBits(n: int) -> List[int]:
    dp = [0] * (n+1)
    offset = 1

    for i in range(1, n+1):
        if offset*2 == i:
            offset = i
        dp[i] = 1 + dp[i-offset]
    return dp

if __name__ == "__main__":
    n = 2
    print(countBits(n))

"""// Java Solution
class Solution {
    public int[] countBits(int n) {
        int[] dp = new int[n + 1];
        int offset = 1;

        for (int i = 1; i <= n; i++) {
            if (offset * 2 == i) {
                offset = i;
            }
            dp[i] = 1 + dp[i-offset];
        }
        return dp;
    }
}"""