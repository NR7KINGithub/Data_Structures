class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: Node, k: int) -> Node:
    if not head or not head.next or k == 0:
        return head
    
    # Find the length of the list and the tail
    length, tail = 1, head
    while tail.next:
        tail = tail.next
        length += 1
    
    # Find the effective rotations needed
    k %= length
    if k == 0:
        return head
    
    # Find the new head (length - k - 1 node is the new tail)
    new_tail_position = length - k - 1
    new_tail = head
    for _ in range(new_tail_position):
        new_tail = new_tail.next
    
    # Update the head and tail
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head
    
    return new_head
    
if __name__ == "__main__":
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    k = 2
    result = rotateRight(head, k)
    while result:
        print(result.val, end=" -> " if result.next else "\n")
        result = result.next