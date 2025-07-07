class Graphs:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()
        

    def __repr__(self):
        str_graph = ""
        for key, value in self.adj_list.items():
            str_graph += f"{key} -> {value}\n"
        return str_graph
    
    def dfs(self, start):
        """Depth-First Search - like Theseus exploring deep into each path"""
        if start not in self.adj_list:
            return []
        
        visited = set()
        stack = [start]
        order = []
        
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbours = self.get_neighbours(node)
                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        stack.append(neighbour)
        return order

    def bfs(self, start, goal=None):
        """Theseus searching for the Minotaur through the labyrinth"""
        if start not in self.adj_list:
            return []
        
        visited = set()
        queue = [start]
        order = []
        path = [start]  # Track Theseus's path
        
        while queue:
            node = queue.pop(0)
            print(f"Exploring room: {node}, Path so far: {path}")
            
            if goal and node == goal:
                print("\n Theseus found the Minotaur!")
                return path
            
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbours = self.get_neighbours(node)
                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        queue.append(neighbour)
                        if goal:  # If we're looking for something specific
                            path.append(neighbour)
        
        if goal:
            print(f"Theseus couldn't find the Minotaur at {goal}")
            return []
        return order

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node exists!")

    def add_edge(self, from_node, to_node, weighted=None):
        if from_node not in self.adj_list:
            self.add_node(from_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weighted is None:
            self.adj_list[from_node].add(to_node)
            # Fixed: add reverse edge when NOT directed
            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:
            self.adj_list[from_node].add((to_node, weighted))
            if not self.directed:
                self.adj_list[to_node].add((from_node, weighted))

    def get_neighbours(self, key_node):
        """Fixed method name to match what bfs() calls"""
        return self.adj_list.get(key_node, set())

    def adj_matrix(self):
        """Convert graph to adjacency matrix"""
        nodes = list(self.adj_list.keys())
        size = len(nodes)
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        
        node_to_index = {node: i for i, node in enumerate(nodes)}
        
        for i, node in enumerate(nodes):
            for neighbor in self.adj_list[node]:
                if isinstance(neighbor, tuple):
                    neighbor_node, weight = neighbor
                    j = node_to_index[neighbor_node]
                    matrix[i][j] = weight
                else:
                    j = node_to_index[neighbor]
                    matrix[i][j] = 1
        
        return matrix, nodes


if __name__ == '__main__':
    # Create Theseus's labyrinth
    graphObj = Graphs()
    
    # Build the maze
    graphObj.add_node("Entrance")
    graphObj.add_node("Hall1")
    graphObj.add_node("Hall2")
    graphObj.add_node("Chamber")
    graphObj.add_node("Minotaur's Lair")
    
    # Connect the rooms
    graphObj.add_edge("Entrance", "Hall1")
    graphObj.add_edge("Hall1", "Hall2")
    graphObj.add_edge("Hall2", "Chamber")
    graphObj.add_edge("Chamber", "Minotaur's Lair")
    graphObj.add_edge("Hall1", "Chamber")  # Shortcut
    
    print("The Labyrinth:")
    print(graphObj)
    
    print("Theseus enters the labyrinth...")
    result = graphObj.bfs("Entrance", "Minotaur's Lair")
    
    print(f"\nFinal result: {result}")
    
    print("\nAlternative: Just exploring without a specific goal:")
    exploration = graphObj.bfs("Entrance")
    print(f"Exploration order: {exploration}")