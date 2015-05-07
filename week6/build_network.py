from Graph import DirectedGraph


def build_network(start, level):
    visited = set()
    queue = []
    visited.add(start)
    queue.append((0, start))
    while len(queue) != 0:
        current_level, current_node = queue.pop(0)
        if current_level > level:
            break
        network = self.get_neighbour_for(current_node)
        for follower in network["folowers"]:
            if follower not in visited:
                queue.add_edge(follower, current_node)
                visited.add(follower)
                queue.append((current_level+1, follower))

                # g.add_edge((cn, following))
