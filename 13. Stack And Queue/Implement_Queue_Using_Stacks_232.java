import java.util.Stack;

class MyQueue {
    private Stack<Integer> inStack;
    private Stack<Integer> outStack;
        public MyQueue() {
            inStack = new Stack<>();
            outStack = new Stack<>();
        }
        
        public void push(int x) {
            inStack.push(x);
        }
        
        public int pop() {
            shiftStacks();
            return outStack.pop();
        }
        
        public int peek() {
            shiftStacks();
            return outStack.peek();
        }
        
        public boolean empty() {
            return inStack.isEmpty() && outStack.isEmpty();
        }
        private void shiftStacks() {
            if (outStack.isEmpty()) {
                while (!inStack.isEmpty()) {
                    outStack.push(inStack.pop());
                }
            }
        }
    }
    
public class Implement_Queue_Using_Stacks_232 {
    public static void main(String[] args) {
        MyQueue obj = new MyQueue();
        obj.push(1);
        obj.push(2);
        int param_2 = obj.pop();
        int param_3 = obj.peek();
        boolean param_4 = obj.empty();

        System.out.println("Popped Element: " + param_2);
        System.out.println("Top Element: " + param_3);
        System.out.println("Queue Empty? " + param_4);
    }
}