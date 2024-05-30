class DirectedGraph:
    def __init__(self):
        self.nodes = []
        self.edges={}
    def add_node (self,node):
        if node in self.nodes:
            return
        self.nodes.append(node)
        self.edges[node]= []
    def add_edges(self,src,dest):
        if src not in self.nodes:
            self.add_node(src)
        if dest not in self.nodes:
            self.add_node(dest)
        adjacent_nodes = self.edges[src]
        if dest in adjacent_nodes:
            return
        self.edges[src].append(dest)
    def adjacent_nodes(self,node):
        return self.edges.get(node, [])
    def remove_node(self,node):
        if node in self.nodes:
            self.nodes.remove(node)
            del(self.edges[node])
        for adjacent_nodes in self.edges.values():
            if node in adjacent_nodes:
                adjacent_nodes.remove(node)
    def display(self):
        print("nodes:", self.nodes)
        print("edges:")
        for node, adjacents in self.edges.items():
            print(node, "->", adjacents)
dg = DirectedGraph()
dg.add_node(1)
dg.add_node(2)
dg.add_edges(1, 2)
dg.add_edges(1, 3)
dg.add_edges(3, 2)
dg.add_edges(2, 4)
dg.display()
print("adjacent nodes to 1:", dg.adjacent_nodes(1))
print("adjacent nodes to 3:", dg.adjacent_nodes(3))
dg.remove_node(2)
print("new Graph:")
dg.display()