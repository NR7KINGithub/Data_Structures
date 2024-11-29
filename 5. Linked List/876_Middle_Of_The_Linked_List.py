class Node:
    def __init__(self, data, next_node=None):
        self.data = data       
        self.next = next_node  
# Function to find the middle node of a linked list
def find_middle(head):
    # Initialize the slow pointer to the head.
    slow = head   
    # Initialize the fast pointer to the head.
    fast = head   
    # Traverse the linked list using the Tortoise and Hare algorithm.
    while fast and fast.next and slow:
        # Move fast two steps.
        fast = fast.next.next 
        # Move slow one step.
        slow = slow.next       
    # Return the slow pointer which is now at the middle node.
    return slow  

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(find_middle(head).data)