from typing import List

class LockingTree:
    def __init__(self, parent: List[int]):
        n = len(parent)
        self.parent = parent
        self.children = [[] for _ in range(n)]
        for i, p in enumerate(parent):
            if p != -1:
                self.children[p].append(i)
        self.locked = [-1] * n

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] != -1:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        self.locked[num] = -1
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num] != -1:
            return False
        cur = num
        while cur != -1:
            if self.locked[cur] != -1:
                return False
            cur = self.parent[cur]
        stack = [num]
        found = []
        while stack:
            node = stack.pop()
            if self.locked[node] != -1:
                found.append(node)
            stack.extend(self.children[node])
        if not found:
            return False
        for node in found:
            self.locked[node] = -1
        self.locked[num] = user
        return True


def run_operations(parent: List[int], ops: List[str], args: List[List[int]]) -> List:
    tree = None
    results = []
    for i, op in enumerate(ops):
        if op == "LockingTree":
            tree = LockingTree(parent)
            results.append(None)
        elif op == "lock":
            res = tree.lock(args[i][0], args[i][1])
            results.append(res)
        elif op == "unlock":
            res = tree.unlock(args[i][0], args[i][1])
            results.append(res)
        elif op == "upgrade":
            res = tree.upgrade(args[i][0], args[i][1])
            results.append(res)
    return results

if __name__ == "__main__":
    parent1 = [-1, 0, 0, 1, 1, 2, 2]
    ops1 = ["LockingTree","lock","unlock","unlock","lock","upgrade","lock"]
    args1 = [[-1,0,0,1,1,2,2], [2,2], [2,3], [2,2], [4,5], [0,1], [0,1]]
    out1 = run_operations(parent1, ops1, args1)
    print(out1)

    parent2 = [-1, 0, 0, 1, 1, 2, 2]
    ops2 = ["LockingTree","lock","unlock","unlock","lock","upgrade","lock"]
    args2 = [[-1,0,0,1,1,2,2], [2,2], [2,3], [2,2], [4,5], [0,1], [0,1]]
    out2 = run_operations(parent2, ops2, args2)
    print(out2)