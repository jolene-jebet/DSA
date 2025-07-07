##class graph: init, dft(depth first traversal), bft(breadth first traversal)
####weight - how much will it take you to traverse from a node to another
#class for graph
class Graph:
    #first method - constructor method 
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    #representation method-print our object
    def __repr__(self):
        #defining a string - holds the dictionary
        str_graphy = ""

        for key, value in self.adj_list.items():
            str_graph +=f"{key} -> {value}"
        return str_graph

    #second method - depth first traversal
    def dft(self):
        visited = set()
        

    #third method - breadth first traversal
    def bft(self):
        pass

    #adding node to graph
    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            #we do this to avoid duplicated
            raise ValueError("Node already exists")

    #adding edge to graph- asking user for source node to destination
    def add_edge(self, source_node, destination_node, weight = None):
        #checking whether souce is in the graph or if it is there, if not, creates it
        if source_node not in self.adj_list:
            self.add_node(source_node)
        if destination_node not in self.adj_list:
            self.add_node(destination_node)

        #checking if graph is weighted
        if weight is None:
            self.adj_list[source_node].add(destination_node)

            if self.directed:
                self.adj_list[destination_node].add(source_node)
        else:
            self.adj_list[source_node].add((destination_node, weight))

            #direction
            if self.directed:
                self.adj_list[destination_node].add((source_node,weight))

    #method for obtaining neighbours(VALUES)
    def obtain_neighbouts(self, key_node):
        return self.adj_list.get(key_node, set())
    
    def adj_matrix(self):
        pass
    
if __name__ == "__main__":
    #creating and object for graph
    graph_obj = Graph()

    print(graph_obj)
