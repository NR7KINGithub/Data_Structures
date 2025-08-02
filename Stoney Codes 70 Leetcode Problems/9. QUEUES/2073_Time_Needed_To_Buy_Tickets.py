from typing import List

def timeRequiredToBuy(tickets: List[int], k: int) -> int:
    result = 0
    for i in range(len(tickets)):
        if i<=k:
            result += min(tickets[i], tickets[k])

        else:
            result += min(tickets[i], tickets[k]-1)
    return result

if __name__ == "__main__":
    tickets = [2,3,2]
    k = 2
    print(timeRequiredToBuy(tickets, k))

"""// Java Solution
class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        int result = 0;
        for (int i = 0; i < tickets.length; i++) {
            if (i <= k) {
                result += Math.min(tickets[i], tickets[k]);
            }
            else {
                result += Math.min(tickets[i], tickets[k]-1);
            }
        }
        return result;
    }
}"""