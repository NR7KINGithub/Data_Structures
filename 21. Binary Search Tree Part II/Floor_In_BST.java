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
public class Floor_In_BST {
    public static int floorInBST(Node<Integer> root, int X) {
        int floor = -1;
        while (root != null) {
            if (root.data == X) {
                return root.data;
            } else if (root.data < X) {
                floor = root.data;
                root = root.right;
            } else {
                root = root.left;
            }
        }
        return floor;
    }
    public static void main(String[] args) {
        Node<Integer> root = new Node<>(10);
        root.left = new Node<>(5);
        root.right = new Node<>(15);
        root.left.left = new Node<>(2);
        root.left.right = new Node<>(6);
        Scanner sc = new Scanner(System.in);
        System.out.println(floorInBST(root, 10));
        sc.close();
    }
}