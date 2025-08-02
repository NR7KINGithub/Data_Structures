class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

if __name__ == "__main__":
    head = Node(4)
    head.next = Node(5)
    head.next.next = Node(1)
    head.next.next.next = Node(9)

    print("Before Deletion:")
    result = head
    while result:
        print(result.val, end=" -> " if result.next else "\n")
        result = result.next

    # Delete node with value 5
    deleteNode(head.next)

    print("After Deletion:")
    result = head
    while result:
        print(result.val, end=" -> " if result.next else "\n")
        result = result.next

"""// Java Solution
class Solution {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}"""