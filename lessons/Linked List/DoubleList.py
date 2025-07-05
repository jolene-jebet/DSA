class Node:
    def __init__(self,value):
        self.value = value

        self.next_node = None
        self.prev_node = None

class DoubleList:
    def __init__(self):
        self.head = None

    def appendNode(self,value):
        if self.head is None:
            new_head_node:Node = Node(value)

            self.head = new_head_node
        else:
            current_node = self.head

            while True:
                if current_node.next_node is None:
                    break
                current_node = current_node.next_node

            new_node:Node = Node(value)

            current_node.next_node = new_node
            new_node.prev_node = current_node

    def prependNode(self,value):
        if self.head is None:
            new_head_node:Node = Node(value)

            self.head = new_head_node
        else:
            new_node:Node = Node(value)

            new_node.next_node = self.head
            self.head.prev_node = new_node

    def removeNode(self,value):
        if self.head is None:
            print("List is empty")
            return
        
        finder = self.head

        if finder.value is value:
            finder.prev_node.next_node = finder.next_node
            finder.next_node.prev_node = finder.prev_node
        else:
            while True:
                if finder.value is value:
                    break
                
                finder = finder.next_node

            finder.prev_node.next_node = finder.next_node
            finder.next_node.prev_node = finder.prev_node
   
    def printListForward(self):
        if self.head is None:
            print("List is empty")
            return
        
        current_node = self.head
        output_list = []
        
        while True:
            output_list.append(str(current_node.value))

            if current_node.next_node is None:
                break

            current_node = current_node.next_node

        print(" -> ".join(output_list))
    
    def printListBack(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            last_node = self.head
            outputList = []

            while True:
                if last_node.next_node is None:
                    break
                last_node = last_node.next_node

            while True:
                outputList.append(str(last_node.value))

                if last_node.prev_node is None:
                    break
                    
                last_node = last_node.prev_node
        
        print(" <- ".join(outputList))

DLL:DoubleList = DoubleList()

DLL.appendNode("Value here")
DLL.appendNode("another here")
DLL.appendNode("and also here")

DLL.printListForward()
DLL.removeNode("another here")
DLL.printListBack()