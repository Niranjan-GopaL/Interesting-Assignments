class Person:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Family:
    def __init__(self):
        self.headOfFamily = None

    def head_of_family(self):
        return self.headOfFamily.name

    def all_nodes(self, node=None):
        if node is None:
            node = self.headOfFamily
        yield node
        for child in node.children:
            yield from self.all_nodes(child)

    def search_node(self, node_name, node=None):
        if node is None:
            node = self.headOfFamily
        if node.name == node_name:
            return node
        for child in node.children:
            result = self.search_node(node_name, child)
            if result is not None:
                return result
        return None

    def all_ancestors(self, node_name):
        node = self.search_node(node_name)
        if node is None:
            return []
        ancestors = []
        parent = node.parent
        while parent is not None:
            ancestors.append(parent.name)
            parent = parent.parent
        ancestors.reverse()
        return ancestors

    def parent(self, node_name):
        node = self.search_node(node_name)
        if node is None:
            return None
        if node.parent is None:
            return None
        return node.parent.name

    def depth(self, node_name):
        node = self.search_node(node_name)
        if node is None:
            return -1
        depth = 0
        parent = node.parent
        while parent is not None:
            depth += 1
            parent = parent.parent
        return depth

    def build_tree(self, inputs):
        persons = {}
        for input_line in inputs:
            name, parent_name, children_names = input_line.split()
            person = Person(name)
            persons[name] = person
            
            
            if parent_name == "None":
                self.headOfFamily = person
            else:
                parent = persons[parent_name]
                person.parent = parent
                parent.add_child(person)
            if children_names != "None":
                children_names = children_names.split(",")
                for child_name in children_names:
                    child = persons[child_name]
                    person.add_child(child)

    def display_tree(self):
        queue = [self.headOfFamily]
        while queue:
            node = queue.pop(0)
            print(node.name, end=" ")
            for child in node.children:
                queue.append(child)
            if queue:  
                print(end="\n")
    
n=int(input())
input_list = [input() for i in range(n)]

fam = Family()
fam.build_tree(input_list)
fam.display_tree()
