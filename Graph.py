class Graph:
    
    def __init__(self):
        self.nodes = []

    def set_node(self,node):
        if node.previous == None:
            self.nodes.append(node)

    def __repr__(self):
        return repr(self.nodes)      