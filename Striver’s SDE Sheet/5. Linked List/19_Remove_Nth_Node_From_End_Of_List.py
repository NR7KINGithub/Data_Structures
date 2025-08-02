class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
# Function to delete the Nth node from the end of the linked list
def DeleteNthNodefromEnd(head, N):
    # Create two pointers, fastp and slowp
    fastp = head
    slowp = head
    # Move the fastp pointer N nodes ahead
    for i in range(N):
        fastp = fastp.next
    # If fastp becomes None, the Nth node from the end is the head
    if fastp is None:
        return head.next
    # Move both pointers until fastp reaches the end
    while fastp.next is not None:
        fastp = fastp.next
        slowp = slowp.next
    # Delete the Nth node from the end
    delNode = slowp.next
    slowp.next = slowp.next.next
    delNode = None
    return head

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
N = 3
result = DeleteNthNodefromEnd(head, N)
while result:
        print(result.data, end=" -> " if result.next else "\n")
        result = result.next

"""// Java Solution
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode fast = head;
        ListNode slow = head;
        for (int i = 0; i < n; i++) {
            fast = fast.next;
        }
        if (fast == null) {
            return head.next;
        }
        while (fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }
        ListNode delNode = slow.next;
        slow.next = slow.next.next;
        delNode = null;
        return head;
    }
}"""