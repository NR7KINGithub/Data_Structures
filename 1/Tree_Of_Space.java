import java.util.*;

class Node {
    String label;
    List<Node> children;
    Node parent;
    int ancestorLocked, descendantLocked, userID;
    boolean isLocked;

    public Node(String name, Node parentNode) {
        this.label = name;
        this.parent = parentNode;
        this.children = new ArrayList<>();
        this.ancestorLocked = 0;
        this.descendantLocked = 0;
        this.userID = 0;
        this.isLocked = false;
    }

    public void addChildren(List<String> childLabels, Node parentNode) {
        for (String childLabel : childLabels) {
            children.add(new Node(childLabel, parentNode));
        }
    }
}

class LockingTree {
    private Node root;
    private Map<String, Node> labelToNode;
    private List<String> outputLog;

    public LockingTree(Node treeRoot) {
        this.root = treeRoot;
        this.labelToNode = new HashMap<>();
        this.outputLog = new ArrayList<>();
    }

    public Node getRoot() {
        return root;
    }

    public void fillLabelToNode(Node currentNode) {
        if (currentNode == null) return;
        
        labelToNode.put(currentNode.label, currentNode);
        for (Node child : currentNode.children) {
            fillLabelToNode(child);
        }
    }

    public void updateDescendant(Node currentNode, int value) {
        for (Node child : currentNode.children) {
            child.ancestorLocked += value;
            updateDescendant(child, value);
        }
    }

    public boolean checkDescendantsLocked(Node currentNode, int id, List<Node> lockedNodes) {
        if (currentNode.isLocked) {
            if (currentNode.userID != id) {
                return false;
            }
            lockedNodes.add(currentNode);
        }

        if (currentNode.descendantLocked == 0) {
            return true;
        }

        boolean result = true;

        for (Node child : currentNode.children) {
            result &= checkDescendantsLocked(child, id, lockedNodes);
            if (!result) {
                return false;
            }
        }

        return result;
    }

    public boolean lockNode(String label, int id) {
        Node targetNode = labelToNode.get(label);
        
        if (targetNode.isLocked) {
            return false;
        }

        if (targetNode.ancestorLocked != 0 || targetNode.descendantLocked != 0) {
            return false;
        }

        Node currentNode = targetNode.parent;

        while (currentNode != null) {
            currentNode.descendantLocked++;
            currentNode = currentNode.parent;
        }

        updateDescendant(targetNode, 1);
        targetNode.isLocked = true;
        targetNode.userID = id;

        return true;
    }

    public boolean unlockNode(String label, int id) {
        Node targetNode = labelToNode.get(label);

        if (!targetNode.isLocked) {
            return false;
        }

        if (targetNode.isLocked && targetNode.userID != id) {
            return false;
        }

        Node currentNode = targetNode.parent;

        while (currentNode != null) {
            currentNode.descendantLocked--;
            currentNode = currentNode.parent;
        }

        updateDescendant(targetNode, -1);
        targetNode.isLocked = false;

        return true;
    }

    public boolean upgradeNode(String label, int id) {
        Node targetNode = labelToNode.get(label);

        if (targetNode.isLocked) {
            return false;
        }

        if (targetNode.ancestorLocked != 0 || targetNode.descendantLocked == 0) {
            return false;
        }

        List<Node> lockedDescendants = new ArrayList<>();

        if (checkDescendantsLocked(targetNode, id, lockedDescendants)) {
            for (Node lockedDescendant : lockedDescendants) {
                unlockNode(lockedDescendant.label, id);
            }
        } else {
            return false;
        }

        lockNode(label, id);
        return true;
    }

    public void processQueries(List<Query> queries) {
        for (Query query : queries) {
            int opcode = query.opcode;
            String nodeLabel = query.nodeLabel;
            int userId = query.userId;

            switch (opcode) {
                case 1:
                    if (lockNode(nodeLabel, userId)) {
                        outputLog.add("true");
                    } else {
                        outputLog.add("false");
                    }
                    break;
                case 2:
                    if (unlockNode(nodeLabel, userId)) {
                        outputLog.add("true");
                    } else {
                        outputLog.add("false");
                    }
                    break;
                case 3:
                    if (upgradeNode(nodeLabel, userId)) {
                        outputLog.add("true");
                    } else {
                        outputLog.add("false");
                    }
                    break;
            }
        }
    }

    public void printOutputLog() {
        for (String result : outputLog) {
            System.out.println(result);
        }
    }
}

class Query {
    int opcode;
    String nodeLabel;
    int userId;

    public Query(int opcode, String nodeLabel, int userId) {
        this.opcode = opcode;
        this.nodeLabel = nodeLabel;
        this.userId = userId;
    }
}

public class Tree_Of_Space {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int numNodes = scanner.nextInt();
        int numChildren = scanner.nextInt();
        int numQueries = scanner.nextInt();

        List<String> nodeLabels = new ArrayList<>();
        for (int i = 0; i < numNodes; i++) {
            nodeLabels.add(scanner.next());
        }

        Node rootNode = new Node(nodeLabels.get(0), null);
        rootNode = buildTree(rootNode, numChildren, nodeLabels);

        LockingTree lockingTree = new LockingTree(rootNode);
        lockingTree.fillLabelToNode(lockingTree.getRoot());

        List<Query> queries = new ArrayList<>();
        for (int i = 0; i < numQueries; i++) {
            int opcode = scanner.nextInt();
            String nodeLabel = scanner.next();
            int userId = scanner.nextInt();
            queries.add(new Query(opcode, nodeLabel, userId));
        }

        lockingTree.processQueries(queries);
        lockingTree.printOutputLog();
        
        scanner.close();
    }

    public static Node buildTree(Node root, int numChildren, List<String> nodeLabels) {
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);

        int startIndex = 1;

        while (!queue.isEmpty()) {
            Node currentNode = queue.poll();

            if (startIndex >= nodeLabels.size()) {
                continue;
            }

            List<String> tempChildrenLabels = new ArrayList<>();

            for (int i = startIndex; i < startIndex + numChildren && i < nodeLabels.size(); i++) {
                tempChildrenLabels.add(nodeLabels.get(i));
            }

            currentNode.addChildren(tempChildrenLabels, currentNode);
            startIndex += numChildren;

            for (Node child : currentNode.children) {
                queue.offer(child);
            }
        }

        return root;
    }
}

/*
INPUT FORMAT:
n = total number of nodes
m = number of children per node
q = number of queries
next 'n' lines = node name in string
next 'q' lines = queries with (opcode, string, uid)
opcode => 1 = Lock, 2 = Unlock, 3 = Upgrade

EXAMPLE INPUT:
7
2
5
World
Asia
Africa
China
India
SouthAfrica
Egypt
1 China 9
1 India 9
3 Asia 9
2 India 9
2 Asia 9

EXPECTED OUTPUT:
true
true
true
false
true
*/