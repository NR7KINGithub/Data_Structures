import java.util.*;

class TreeNode<T> {
    T data;
    TreeNode<T> left;
    TreeNode<T> right;

    TreeNode(T data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}
public class Floor_In_BST {
    public static int floorInBST(TreeNode<Integer> root, int X) {
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
        TreeNode<Integer> root = new TreeNode<>(10);
        root.left = new TreeNode<>(5);
        root.right = new TreeNode<>(15);
        root.left.left = new TreeNode<>(2);
        root.left.right = new TreeNode<>(6);
        Scanner sc = new Scanner(System.in);
        System.out.println(floorInBST(root, 10));
        sc.close();
    }
}