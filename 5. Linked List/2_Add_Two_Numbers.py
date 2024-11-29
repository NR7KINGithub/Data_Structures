class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1, l2):
    dummy = Node()
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        curr.next = Node(total % 10)

        curr = curr.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next
    
l1 = Node(2, Node(4, Node(3)))
l2 = Node(5, Node(6, Node(4)))
result = addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" -> " if result.next else "\n")
    result = result.next