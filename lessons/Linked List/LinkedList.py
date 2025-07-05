class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self,new_data): # insert at beginning
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        tem = self.head

        while tem:
            print(f'{tem.data}',end=' ')
            tem = tem.next    

if __name__ == "__main__":
    Llist = LinkedList()
    list = ["New","Data","Is","New","Data"]
    
    for index in range(len(list) - 1,-1,-1):
        Llist.prepend(list[index])

    Llist.print()
        
# class LinkedList:
#     def __init__(self,value,nextNode = None):
#         self.value = value
#         self.nextNode = nextNode

# node1 = LinkedList('1 1')
# node2 = LinkedList('1 2')
# node3 = LinkedList('1 3')
# node4 = LinkedList('1 4')
# node5 = LinkedList('1 5')
# node6 = LinkedList('1 6')
# node7 = LinkedList('1 7')
# node8 = LinkedList('1 8')

# node1.nextNode = node2
# node2.nextNode = node3
# node3.nextNode = node4
# node4.nextNode = node5
# node5.nextNode = node6
# node6.nextNode = node7
# node7.nextNode = node8

# currentNode = node1
# i = 0

# while True:
#     print(f"Node {i + 1} >>>", currentNode.value)
#     i += 1

#     if currentNode.nextNode is None:
#         print('\nFinal node')
#         break

#     currentNode = currentNode.nextNode
    
