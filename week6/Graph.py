
class DirectedGraph:
    def __init__(self):
        self.connections = {}
        self.nodes = []

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            self.connections[node] = []

    def add_edge(self, node_a, node_b):
        self.add_node(node_a)
        self.add_node(node_b)
        self.connections[node_a] += [node_b]

    def get_neighbour_for(self, node):
        return self.connections[node]

    def path_between(self, node_a, node_b):
        visited = set()
        queue = []
        queue.append(node_a)
        visited.add(node_a)
        path_to = {}
        path_to[node_a] = None
        found = False
        path_length = 0

        while len(queue) != 0:
            current_node = queue.pop(0)
            if current_node == node_b:
                found = True
                break

            for neighbour in self.connections[current_node]:
                if neighbour not in visited:
                    path_to[neighbour] = current_node
                    visited.add(neighbour)
                    queue.append(neighbour)
        if found:
            while path_to[node_b] is not None:
                path_length += 1
                node_b = path_to[node_b]

        if path_length != 0:
            return True
        return False
