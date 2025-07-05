from DoubleList import Node

class CircularList:
    def __init__(self):
        self.head = None

    def appendNode(self,value):
        new_head_node = Node(value)

        if self.head is None:
            new_head_node.next_node = new_head_node
            new_head_node.prev_node = new_head_node

            self.head = new_head_node
        else:
            new_node:Node = Node(value)
            current_node = self.head

            while True:
                if current_node.next_node is None:
                    break

                current_node = current_node.next_node

            current_node.next_node = new_node
            new_node.prev_node = current_node
        
    def prependNode(self,value):
        pass
        