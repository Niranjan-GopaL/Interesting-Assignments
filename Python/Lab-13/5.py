# It has 3 property 
class Person:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return self.name


# Basically this class is A TREE
class Family:
    def __init__(self, headOfFamily):
        self.headOfFamily = headOfFamily

    def allNodes(self, node):
        nodes = [node]
        for child in node.children:
            nodes += self.allNodes(child)
        return nodes

    def searchNode(self, node, name):
        if node.name == name:
            return node
        for child in node.children:
            result = self.searchNode(child, name)
            if result is not None:
                return result
        return None

    def allAncestors(self, node):
        ancestors = []
        parent = node.parent
        while parent is not None:
            ancestors.append(parent)
            parent = parent.parent
        return ancestors

    def parent(self, node):
        return node.parent

    def depth(self, node):
        depth = 0
        parent = node.parent
        while parent is not None:
            depth += 1
            parent = parent.parent
        return depth

    # THIS PRINTS THE ENTIRE TREE IN THIS FORMAT:
    '''
    |---Alice
    |   |---Bob
    |   |   |---Diane
    |   |   |---Edward
    |   |---Charlie
    |   |   |---Frank  
    ''' 
    def __str__(self):
        def print_tree(node, level=0):
            # 
            tree_str = "|   " * level + "|---" + str(node) + "\n"
            for child in node.children:
                tree_str += print_tree(child, level + 1)
            return tree_str

        return print_tree(self.headOfFamily)


# Create people
obj_alice = Person("Alice")
obj_bob = Person("Bob")
obj_charlie = Person("Charlie")
obj_diane = Person("Diane")
obj_edward = Person("Edward")
obj_frank = Person("Frank")


# Build the family tree
obj_alice.add_child(obj_bob)
obj_alice.add_child(obj_charlie)
obj_bob.add_child(obj_diane)
obj_bob.add_child(obj_edward)
obj_charlie.add_child(obj_frank)


# Create a family object for Alice with Alice as head of family
family = Family(obj_alice)


# Print the family tree using the __str__ method of the Family class
print(family)
# Find a node by name
print(family.searchNode(family.headOfFamily, "Charlie"))
# Get all ancestors of a node
print(family.allAncestors(obj_diane))
# Get the parent of a node
print(family.parent(obj_diane))
# Get the depth of a node
print(family.depth(obj_frank))
