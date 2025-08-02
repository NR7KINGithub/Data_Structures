class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
# Function to reverse linked list using 3 pointer approach
def Reverse_Linked_List(head):
    # Initialize 'temp' at the head of the linked list
    temp = head
    # Initialize 'prev' to None, representing the previous node 
    prev = None
    while temp is not None:
        # Store the next node in 'front' to preserve the reference
        front = temp.next
        # Reverse the direction of the current node's 'next' pointer to point to 'prev'
        temp.next = prev
        # Move 'prev' to the current  node, for the next iteration
        prev = temp
        # Move 'temp' to 'front' node advancing traversal
        temp = front
    # Return the new head of the reversed linked list
    return prev

head = Node(1, Node(3, Node(2, Node(4))))

print("Original Linked List:")
result = head
while result:
    print(result.data, end=" -> " if result.next else "\n")
    result = result.next

head = Reverse_Linked_List(head)

print("Reversed Linked List:")
result = head
while result:
    print(result.data, end=" -> " if result.next else "\n")
    result = result.next

"""// Java Solution
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode current = head;
        ListNode prev = null;
        while (current != null) {
            ListNode next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        return prev;
    }
}"""