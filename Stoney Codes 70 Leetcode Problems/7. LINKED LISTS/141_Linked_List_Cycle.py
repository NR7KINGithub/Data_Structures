from typing import Optional

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def hasCycle(head: Optional[Node]) -> bool:
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True

    return False

"""// Java Solution
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }
}"""