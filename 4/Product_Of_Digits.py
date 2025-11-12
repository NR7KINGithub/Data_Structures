def productOfDigits(n: int) -> int:
    result = 1
    while n > 0:
        result = result * (n % 10)
        n //= 10
    return result

if __name__ == "__main__":
    n = 5244
    print(productOfDigits(n))

"""// Java Solution
class Solution {
    public static int productOfDigits(int n) {
        int result  = 0;
        while (n > 0) {
            result *= n % 10;
            n /= 10;
        }
        return result;
    }
    
    public static void main(String[] args) {
        int n = 5244;
        System.out.println(productOfDigits(n));   
    }
}
"""