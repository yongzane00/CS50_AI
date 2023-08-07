class Node:
    def __init__(self, state, parent=None):
        self.state = state  # The state represented by the node
        self.parent = parent  # Parent node
        self.frontier = []  # List of child nodes

    def add_frontier(self, child_node):
        self.frontier.append(child_node)

# Create nodes and build a sample tree
root_node = Node("A")
child_node1 = Node("B", parent=root_node)
child_node2 = Node("C", parent=root_node)

child_node1.add_frontier(Node("D", parent=child_node1))
child_node1.add_frontier(Node("E", parent=child_node1))

child_node2.add_frontier(Node("F", parent=child_node2))

# Accessing node properties
print("Root Node State:", root_node.state)
print("Child Node 1 Parent State:", child_node1.parent.state)
print("Child Node 1 Frontier States:", [node.state for node in child_node1.frontier])
