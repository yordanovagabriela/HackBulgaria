def build_network(start, level):
    visited = set()
    queue = []
    visited.add(start)
    queue.append((0, start))
    while len(queue) != 0:
        current_level, current_node = queue.pop(0)
        if current_level > level:
            break
        network = get_network_for(cn)
        for follower in network["folowers"]:
            if follower not in visited:
                g.add_edge(follower, cn)
                visited.add(follower)
                queue.append((cl+1, follower))

                # g.add_edge((cn, following))
