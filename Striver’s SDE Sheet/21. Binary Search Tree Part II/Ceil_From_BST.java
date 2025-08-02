import java.util.*;

class Node<T> {
    T data;
    Node<T> left;
    Node<T> right;

    Node(T data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}
public class Ceil_From_BST {
    public static int findCeil(Node<Integer> node, int x) {
        int ceil = -1;
        while (node != null) {
            if (node.data == x) {
                return node.data;
            } else if (node.data < x) {
                node = node.right;
            } else {
                ceil = node.data;
                node = node.left;
            }
        }
        return ceil;
    }
   public static void main(String[] args) {
        Node<Integer> root = new Node<>(8);
        root.left = new Node<>(5);
        root.right = new Node<>(10);
        root.left.left = new Node<>(2);
        root.left.right = new Node<>(6);
        root.left.right.right = new Node<>(7);
        Scanner sc = new Scanner(System.in);
        System.out.println(findCeil(root, 7));
        sc.close();
    }
}