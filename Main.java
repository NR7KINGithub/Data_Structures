import java.util.Stack;

public class Main {
    public static void swap1(int a, int b) {
        System.out.println("Before Swap: a="+a+" b="+b);
        a = a + b;
        b = a - b;
        a = a - b;
        System.out.println("After Swap: a="+a+" b="+b);
    }
    
    public static void swap2(int a, int b) {
        System.out.println("Before Swap: a="+a+" b="+b);
        int temp = a;
        a = b;
        b = temp;
        System.out.println("After Swap: a="+a+" b="+b);
    }
    
    public static void evenOdd(int n) {
        if (n % 2 == 0) {
            System.out.println("Even");
        }
        else {
            System.out.println("Odd");
        }
    }
    
    public static void leapYear(int y) {
        if (y % 400 == 0 || (y % 4 == 0 && y % 100 != 0)) {
            System.out.println("Leap Year");
        }
        else {
            System.out.println("Not Leap Year");
        }
    }
    
    public static boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
    
    public static boolean isPalindrome(int n) {
        if (n < 0) {
            return false;
        }
        
        int num = n;
        int rev = 0;
        while (num != 0) {
            int rem = num % 10;
            rev = rev * 10 + rem;
            num /= 10;
        }
        
        return n == rev;
    }
    
    public static boolean isArmstrong(int n) {
        int l = String.valueOf(n).length();
        int num = n;
        int sum = 0;
        
        while(num != 0) {
            int rem = num % 10;
            sum += Math.pow(rem, l);
            num /= 10;
        }
        return n == sum;
    }
    
    public static boolean strong(int n) {
        int num = n;
        int sum = 0;
        
        while(num != 0) {
            int rem = num % 10;
            sum += factorial(rem);
            num /= 10;
        }
        return n == sum;
    }
    
    public static boolean perfect(int n) {
        if (n <= 0) {
            return false;
        }
        
        int sum = 0;
        for (int i = 1; i < n; i++) {
            if (n % i == 0) {
                sum += i;
            }
        }
        return n == sum;
    }
    
    public static boolean niven(int n) {
        if (n <= 0) {
            return false;
        }
        
        int num = n;
        int sum = 0;
        while (num != 0) {
            int rem = num % 10;
            sum += rem;
            num /= 10;
        }
        return n % sum == 0;
    }
    
    public static void fibonacci(int n) {
        int i = 1, a = -1, b = 1;
        System.out.print("Fibonacci Series Upto "+n+" Terms: ");
        while ( i <= n) {
            int c = a + b;
            System.out.print(c+" ");
            a = b;
            b = c;
            i++;
        }
    }
    
    public static int factorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        int fact = 1;
        for (int i = 2; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }

    public static String reverse(String s) {
        Stack<Character> st = new Stack<>();
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) != ' ') {
                st.push(s.charAt(i));
            }

            else {
                while(!st.isEmpty()) {
                    result.append(st.pop());
                }

                result.append(" ");
            }
        }

        while(!st.isEmpty()) {
            result.append(st.pop());
        }
        return result.toString();
    }

    public static void reverseArray(int[] arr) {
        int start = 0;
        int end = arr.length - 1;

        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    public static void matrix(int[][] A, int[][] B) {
        int r1 = A.length;
        int c1 = A[0].length;
        int r2 = B.length;
        int c2 = B[0].length;
        
        if (c1 != r2) {
            throw new IllegalArgumentException("Incompatible Matrix Dimensions");
        }

        int[][] C = new int[r1][c2];
        for(int i = 0; i < r1; i++) {
            for (int j = 0; j < c2; j++) {
                for (int k = 0; k < c1; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }

        for(int i = 0; i < C.length; i++) {
            for (int j = 0; j < C[0].length; j++) {
                System.out.print(C[i][j] + "    ");
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        swap1(7, 10);
        swap2(10, 7);
        evenOdd(33);
        leapYear(2025);
        System.out.println(isPrime(21));
        System.out.println(isPalindrome(343));
        System.out.println(isArmstrong(153));
        System.out.println(strong(145));
        System.out.println(perfect(28));
        System.out.println(niven(18));
        fibonacci(10); System.out.println();
        System.out.println(factorial(5));
        System.out.println(reverse("Hello World"));
        int[][] A = { {3, -2, 5}, {3, 0, 4} }; int[][] B = { {2, 3}, {-9, 0}, {0, 4} };
        matrix(A, B);
        int[] arr = {1, 2, 3, 4, 5}; reverseArray(arr);
    }
}