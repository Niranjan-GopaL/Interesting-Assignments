class Person:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

class Family:
    def __init__(self, headOfFamily):
        self.headOfFamily = headOfFamily
        
    def allNodes(self, node):
        nodes = [node.name]
        for child in node.children:
            nodes.extend(self.allNodes(child))
        return nodes
    
    def searchNode(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        for child in node.children:
            result = self.searchNode(child, name)
            if result is not None:
                return result
        return None
    
    def allAncestors(self, node):
        ancestors = []
        current = node.parent
        while current is not None:
            ancestors.append(current.name)
            current = current.parent
        return ancestors
    
    def parent(self, node):
        if node.parent is not None:
            return node.parent.name
        else:
            return None
    
    def depth(self, node):
        current = node
        depth = 0
        while current.parent is not None:
            current = current.parent
            depth += 1
        return depth
    
    def get_family_tree(self, node, level):
        if node is None:
            return ''
        result = node.name + '\n'
        for child in node.children:
            result += ' ' * level + self.get_family_tree(child, level+1)
        return result

# read input
n = int(input())

# create people
people = {}
for i in range(n):
    name, parent, children = input().split()
    if name not in people:
        people[name] = Person(name)
    if parent != 'None':
        if parent not in people:
            people[parent] = Person(parent)
        people[name].parent = people[parent]
        people[parent].children.append(people[name])
    if children != 'None':
        children = children.split(',')
        for child in children:
            if child not in people:
                people[child] = Person(child)
            people[name].children.append(people[child])

# create family tree
headOfFamily = people[input().strip()]
family = Family(headOfFamily)

# output family tree
print(family.get_family_tree(headOfFamily, 0).strip())
