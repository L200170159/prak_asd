class Node: 

    def __init__(self, data): 

        self.data = data 

        self.prev = None

class Nodes: 

    def __init__(self): 

        self.head = None

    def awal(self, new_data):

        print("tambah simpul awal", new_data)

        new_node = Node(new_data) 

        new_node.next = self.head 

        if self.head is not None: 

            self.head.prev = new_node 

        self.head = new_node 

    def akhir(self, new_data):

        print("tambah simpul akhir", new_data)

        new_node = Node(new_data) 

        new_node.next = None

        if self.head is None: 

            new_node.prev = None

            self.head = new_node 

            return 

        last = self.head 

        while(last.next is not None): 

            last = last.next

        last.next = new_node 

        new_node.prev = last 

        return

    def printList(self, node): 

        print("\nDepan :")

        while(node is not None): 

            print(" % d" %(node.data))

            last = node 

            node = node.next

        print("\nBelakang :")

        while(last is not None): 

            print(" % d" %(last.data)) 

            last = last.prev 

Ns = Nodes() 

Ns.awal(4)  

Ns.awal(1)

Ns.akhir(0)

Ns.akhir(4) 

Ns.printList(Ns.head) 
