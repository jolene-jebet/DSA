class Graph:
    def __init__(self, directed=False):
        """
        Creates a new graph.

        :param directed: Whether the graph is directed or not
        """
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        """
        Returns a string representation of the graph
        """
        graph_str = ""

        for node, neighbors in self.adj_list.items():
            graph_str += f"{node} -> {neighbors}\n"

        return graph_str

    def add_node(self, node):
        """
        Adds a node to the graph.

        :param node: The node to add
        """
        if node not in self.adj_list.keys():
            self.adj_list[node] = set()
        else:
            raise ValueError("Node exists already")

    def remove_node(self, node):
        """
        Removes a node from the graph.

        :param node: The node to remove
        """
        if node not in self.adj_list.keys():
            raise ValueError("Node does not exist")
        
        for neighbors in self.adj_list.values():
            neighbors.discard(node)

        del self.adj_list[node]

    def add_edge(self, from_node, to_node, weight=None):
        """
        Adds an edge between two nodes in the graph.

        :param from_node: The node the edge starts from
        :param to_node: The node the edge goes to
        :param weight: The weight of the edge
        """
        if from_node not in self.adj_list:
            self.add_node(from_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
            self.adj_list[from_node].add(to_node)
            
            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:
            self.adj_list[from_node].add(to_node, weight)
            
            if not self.directed:
                self.adj_list[from_node].add((from_node, weight))

    def remove_edge(self, from_node, to_node):
        """
        Removes an edge between two nodes in the graph.

        :param from_node: The node the edge starts from
        :param to_node: The node the edge goes to
        """
        if from_node in self.adj_list:
            if to_node in self.adj_list[from_node]:
                self.adj_list[from_node].remove(to_node)
            else:
                raise ValueError("Edge does not exist")
            
            if not self.directed:
                if from_node in self.adj_list[to_node]:
                    self.adj_list[to_node].remove(from_node)
        else:
            raise ValueError("Edge does not exists")

    def get_neighbors(self, node):
        """
        Returns the neighbors of a given node in the graph.

        :param node: The node to get neighbors for
        :return: A set of the node's neighbors
        """
        return self.adj_list.get(node, set())

    def has_node(self, node):
        """
        Checks if a node exists in the graph.

        :param node: The node to check
        :return: True if the node exists, False otherwise
        """
        return node in self.adj_list

    def has_edge(self, from_node, to_node):
        """
        Checks if an edge exists between two nodes in the graph.

        :param from_node: The node the edge starts from
        :param to_node: The node the edge goes to
        :return: True if the edge exists, False otherwise
        """
        if from_node in self.adj_list:
            return to_node in self.adj_list[from_node]
        return False

    def get_nodes(self):
        """
        Returns a list of all nodes in the graph.
        """
        return list(self.adj_list.keys())

    def get_edges(self):
        """
        Returns a list of all edges in the graph.
        """
        edges = []
        for from_node, neighbors in self.adj_list.items():
            for neighbor in neighbors:
                if isinstance(neighbor, tuple):
                    neighbor = neighbor[0]
                edges.append((from_node, neighbor))
        return edges

    def BFS(self, start):
        """
        Performs a breadth-first search on the graph starting from the given node.

        :param start: The node to start the search from
        :return: A list of nodes in the order they were visited
        """
        visited = set()
        queue = [start]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbors(node)

                for neighbor in neighbors:
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        queue.append(neighbor)

        return order
    
    def DFS(self, start):
        """
        Performs a depth-first search on the graph starting from the given node.

        :param start: The node to start the search from
        :return: A list of nodes in the order they were visited
        """
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbors(node)

                for neighbor in sorted(neighbors, reverse=True):
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        stack.append(neighbor)

        return order
