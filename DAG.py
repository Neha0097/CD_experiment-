class Node:
    def __init__(self, op=None, left=None, right=None, value=None):
        self.op = op
        self.left = left
        self.right = right
        self.value = value
        self.labels = []

class DAG:
    def __init__(self):
        self.nodes = []

    def find_node(self, op, left, right):
        for node in self.nodes:
            if node.op == op and node.left == left and node.right == right:
                return node
        return None

    def get_leaf(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        new_node = Node(value=value)
        self.nodes.append(new_node)
        return new_node

    def create_node(self, op, left, right):
        existing = self.find_node(op, left, right)
        if existing:
            return existing

        new_node = Node(op, left, right)
        self.nodes.append(new_node)
        return new_node

    def add_expression(self, lhs, rhs):
        tokens = rhs.split()

        if len(tokens) == 1:
            node = self.get_leaf(tokens[0])
        else:
            left = self.get_leaf(tokens[0])
            op = tokens[1]
            right = self.get_leaf(tokens[2])
            node = self.create_node(op, left, right)

        node.labels.append(lhs)

    def display(self):
        print("\nDAG Representation:\n")
        for i, node in enumerate(self.nodes):
            if node.op:
                print(f"Node {i}: ({node.left.value or node.left.op} {node.op} {node.right.value or node.right.op}) -> {node.labels}")
            else:
                print(f"Node {i}: {node.value} -> {node.labels}")


# -------- MAIN --------
dag = DAG()

n = int(input("Enter number of expressions: "))

for _ in range(n):
    expr = input("Enter expression (e.g., a = b + c): ")
    lhs, rhs = expr.split("=")
    dag.add_expression(lhs.strip(), rhs.strip())

dag.display()
