from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    dummy = Node(val = 1)
    curr = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            curr = list1
            list1 = list1.next
            
        else:
            curr.next = list2
            curr = list2
            list2 = list2.next
            
    curr.next = list1 if list1 else list2
    return dummy.next              

list1 = Node(1, Node(2, Node(4)))
list2 = Node(1, Node(3, Node(4)))
merged = mergeTwoLists(list1, list2)
while merged:
    print(merged.val, end=" -> " if merged.next else "\n")
    merged = merged.next