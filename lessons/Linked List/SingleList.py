class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleList:
    def __init__(self, headNode: Node, tailNode: Node = None):
        self.headNode = headNode
        self.tailNode = tailNode or self._findTail(headNode)
    
    def _findTail(self, node):
        current = node
        while current and current.next:
            current = current.next
        return current
    
    def findNode(self,data):
        if self.headNode.data == data:
            return self.headNode
        
        if self.headNode and self.headNode.next:
            current = self.headNode

            while True:
                if current.data == data:
                    break
                current = current.next
            
            if current == self.headNode:
                return None
            else:
                return current

        else:
            if self.headNode.data == data:
                return self.headNode
            else: return None
            

    def prepend(self,Node:Node):
        Node.next = self.headNode
        self.headNode = Node
    
    def insertAtEnd(self, newNode: Node):
        if self.headNode is None:
            self.headNode = newNode
            self.tailNode = newNode
        else:
            if self.tailNode is not None:
                self.tailNode.next = newNode
                self.tailNode = newNode
            else:
                current = self.headNode
                while current.next is not None:
                    current = current.next
                current.next = newNode
                self.tailNode = newNode  # update tailNode


    def inBetween(self,middleNode:Node,newNode:Node):
        if middleNode is None:
            print("No node entered")
        else:
            newNode.next = middleNode.next
            middleNode.next = newNode

    def deleteHead(self):
        if self.headNode: self.headNode = self.headNode.next
        else: print("No nodes in list")

    def deleteNode(self,data):
        beforeNode = self.headNode
        nodetodelete:Node = None

        while beforeNode:
            if beforeNode.next.data is data:
                nodetodelete = beforeNode.next
                break
            beforeNode = beforeNode.next

        if nodetodelete:
            beforeNode.next = nodetodelete.next
        else:
            print("Node not found")


    def print(self):
        currentNode = self.headNode

        while True:
            print(currentNode.data)

            if currentNode.next == None:
                break

            currentNode = currentNode.next

node1:Node = Node(1)
node2:Node = Node(2)
node3:Node = Node(3)
node4:Node = Node(4)
node5:Node = Node(5)
node6:Node = Node(10)
node7:Node = Node(15)

node1.next = node2
node2.next = node3
node3.next = node4

Slist:SingleList = SingleList(node1)

print(Slist.tailNode.data)

print("Insert at beginning")
Slist.prepend(node5)
Slist.print()

print("Appending")
Slist.insertAtEnd(node6)
Slist.print()
print("In between")
Slist.inBetween(node3,node7)
Slist.print()
print("Delete head")
Slist.deleteHead()
Slist.print()
print("Delete node")
Slist.deleteNode(2)
Slist.deleteNode(3)
Slist.print()
print("Find node")
nodeFinder:Node | None = Slist.findNode(1)

print("Node found " + str(nodeFinder.data) if nodeFinder.data else "No node found")