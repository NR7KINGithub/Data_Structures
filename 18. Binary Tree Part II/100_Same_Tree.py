# Definition for a binary tree node
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    def same(p, q):
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        if p.val != q.val:
            return False

        return same(p.left, q.left) and \
                same(p.right, q.right)

    return same(p,q)

p = Node(1)
p.left = Node(2)
p.right = Node(2)
p.left.left = Node(3)
p.right.right = Node(3)
p.left.right = Node(4)
p.right.left = Node(4)


q = Node(1)
q.left = Node(2)
q.right = Node(2)
q.left.left = Node(3)
q.right.right = Node(3)
q.left.right = Node(4)
q.right.left = Node(4)

print(isSameTree(p, q))