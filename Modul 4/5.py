class Node: 

    def __init__(self, data): 

        self.data = data 

        self.next = None

class LinkedList: 

    def __init__(self): 

        self.head = None

    def pushAw(self, new_data): 

        new_node = Node(new_data) 

        new_node.next = self.head 

        self.head = new_node

        return self.head

    def search(self, x): 

        current = self.head 

        while current != None: 

            if current.data == x: 

                return "True"

            current = current.next

        return "False"

    def display(self):

        current = self.head

        while current is not None:

            print(current.data, end = ' ')

            current = current.next   

    

LL = LinkedList() 

LL.pushAw(14)

LL.pushAw(4)

LL.pushAw(1)

LL.pushAw(19)

LL.pushAw(99)

LL.pushAw(16)



