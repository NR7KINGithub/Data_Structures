from typing import List

def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    arr.sort()
    n = len(arr)
    min_diff = float('inf')
    result = []

    for i in range(1, n):
        min_diff = min(min_diff, arr[i] - arr[i-1])

    for i in range(1, n):
        if arr[i] - arr[i-1] == min_diff:
            result.append([arr[i-1], arr[i]])

    return result

if __name__ == "__main__":
    arr = [4,2,1,3]
    print(minimumAbsDifference(arr))

"""// Java Solution
class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);
        int n = arr.length;
        int min_diff = Integer.MAX_VALUE;
        List<List<Integer>> result = new ArrayList<>();

        for(int i = 1; i < n; i++) {
            min_diff = Math.min(min_diff, arr[i] - arr[i-1]);
        }

        for(int i = 1; i < n; i++) {
            if (arr[i] - arr[i-1] == min_diff) {
                List<Integer> pair = new ArrayList<>();
                pair.add(arr[i - 1]);
                pair.add(arr[i]);
                result.add(pair);
            }
        }
        return result;
    }
}"""