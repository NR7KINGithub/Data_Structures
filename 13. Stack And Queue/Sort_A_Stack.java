import java.util.*;

public class Sort_A_Stack {
    // Function to sort the stack
    public static void sortStack(Stack<Integer> stack) {
        // Base case: if stack is empty, return
        if (stack.isEmpty()) {
            return;
        }
        // Step 1: Remove the top element
        int topElement = stack.pop();
        // Step 2: Recursively sort the remaining stack
        sortStack(stack);
        // Step 3: Insert the removed element back in sorted order
        insertInSortedOrder(stack, topElement);
    }

    // Helper function to insert an element in a sorted stack
    private static void insertInSortedOrder(Stack<Integer> stack, int element) {
        // Base case: if stack is empty or the top element is greater than the current element
        if (stack.isEmpty() || stack.peek() <= element) {
            stack.push(element);
            return;
        }
        // Step 1: Remove the top element
        int topElement = stack.pop();
        // Step 2: Recursively call to insert the element
        insertInSortedOrder(stack, element);
        // Step 3: Push the top element back
        stack.push(topElement);
    }

    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(5);
        stack.push(-2);
        stack.push(9);
        stack.push(-7);
        stack.push(3);

        System.out.println("Original Stack: " + stack);
        sortStack(stack);
        System.out.println("Sorted Stack: " + stack);
    }
}