from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def removeElements(head: Optional[Node], val: int) -> Optional[Node]:
    temp = Node(-1)
    temp.next = head
    current = temp
    
    while current.next != None:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    return temp.next
    
head = Node(1, Node(2, Node(6, Node(3, Node(4, Node(5, Node(6)))))))
val = 6
result = removeElements(head, val)
while result:
    print(result.val, end=" -> " if result.next else "\n")
    result = result.next

"""// Java Solution 
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode temp = new ListNode(-1);
        temp.next = head;
        ListNode current = temp;

        while (current.next != null) {
            if (current.next.val == val) {
                current.next = current.next.next;
            }
            else {
                current = current.next;
            }
        }
        return temp.next;
    }
}"""