# Definition for a binary tree node
class TreeNode(object):
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

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(2)
p.left.left = TreeNode(3)
p.right.right = TreeNode(3)
p.left.right = TreeNode(4)
p.right.left = TreeNode(4)


q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(2)
q.left.left = TreeNode(3)
q.right.right = TreeNode(3)
q.left.right = TreeNode(4)
q.right.left = TreeNode(4)

print(isSameTree(p, q))