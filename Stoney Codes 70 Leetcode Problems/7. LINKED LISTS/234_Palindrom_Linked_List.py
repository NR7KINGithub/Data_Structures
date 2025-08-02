from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: Optional[Node]) -> bool:
        # Find the middle
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Reverse the second half.
        second_half_start = self.reverseList(slow)
        # Compare the first half with the reversed second half.
        first_half_start = head
        while second_half_start:
            if first_half_start.val != second_half_start.val:
                return False
            first_half_start = first_half_start.next
            second_half_start = second_half_start.next
        return True
    # Helper function to reverse a linked list.
    def reverseList(self, head: Optional[Node]) -> Optional[Node]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
head = Node(1, Node(2, Node(2, Node(1))))
print(Solution().isPalindrome(head))

"""// Java Solution
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        
        ListNode second_half_start = reverseList(slow);
        
        ListNode first_half_start = head;
        while (second_half_start != null) {
            if (first_half_start.val != second_half_start.val) {
                return false;
            }
            first_half_start = first_half_start.next;
            second_half_start = second_half_start.next;
        }
        return true;
    }
    
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