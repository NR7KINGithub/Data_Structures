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
public class Ceil_From_BST {
    public static int findCeil(TreeNode<Integer> node, int x) {
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
        TreeNode<Integer> root = new TreeNode<>(8);
        root.left = new TreeNode<>(5);
        root.right = new TreeNode<>(10);
        root.left.left = new TreeNode<>(2);
        root.left.right = new TreeNode<>(6);
        root.left.right.right = new TreeNode<>(7);
        Scanner sc = new Scanner(System.in);
        System.out.println(findCeil(root, 7));
        sc.close();
    }
}