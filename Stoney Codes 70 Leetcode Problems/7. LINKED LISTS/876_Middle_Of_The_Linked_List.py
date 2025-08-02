class Node:
    def __init__(self, data, next_node=None):
        self.data = data       
        self.next = next_node  

def find_middle(head):
    slow = fast = head
    while fast and fast.next and slow:
        fast = fast.next.next 
        slow = slow.next       
    return slow  

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(find_middle(head).data)

"""// Java Solution
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && slow != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow;
    }
}"""