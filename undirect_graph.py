class UndirectedGraph:
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def add_node(self, node):
        if node in self.nodes:
            return
        self.nodes.append(node)
        self.edges[node] = []
    def add_edges(self, src, dest):
        if src not in self.nodes:
            self.add_node(src)
        if dest not in self.nodes:
            self.add_node(dest)
        if dest not in self.edges[src]:
            self.edges[src].append(dest)
        if src not in self.edges[dest]:
            self.edges[dest].append(src)
    def adjacent_nodes(self, node):
        return self.edges.get(node, [])
    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            del self.edges[node]
        for adjacent_nodes in self.edges.values():
            if node in adjacent_nodes:
                adjacent_nodes.remove(node)
    def display(self):
        print("Nodes:", self.nodes)
        print("Edges:")
        for node, adjacents in self.edges.items():
            print(node, "->", adjacents)
ug = UndirectedGraph()
ug.add_node(1)
ug.add_node(2)
ug.add_edges(1, 2)
ug.add_edges(1, 3)
ug.add_edges(3, 2)
ug.add_edges(2, 4)
ug.display()
print("adjacent nodes to 1:",ug.adjacent_nodes(1))
print("adjacent nodes to 3:",ug.adjacent_nodes(3))
ug.remove_node(2)
print("undirected Graph after removing node 2:")
ug.display()
