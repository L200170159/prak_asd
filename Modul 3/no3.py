class Node: 

    def __init__(self, data): 

        self.data = data 

        self.next = None

class Nodes: 

    def __init__(self): 

        self.head = None

    def tambahDepan(self, new_data): 

        new_node = Node(new_data) 

        new_node.next = self.head 

        self.head = new_node

    def tambahAkhir(self, data):

        if (self.head == None):

            self.head = Node(data)

        else:

            current = self.head

            while (current.next != None):

                current = current.next

            current.next = Node(data)

        return self.head

    def tambah(self,data,posisinya):

        node = Node(data)

        if not self.head:

            self.head = node

        elif posisinya==0:

            node.next = self.head

            self.head = node

        else:

            prev = None

            current = self.head

            current_posisinya = 0

            while(current_posisinya < posisinya) and current.next:

                prev = current

                current = current.next

                current_posisinya +=1

            prev.next = node

            node.next = current

        return self.head

    def hapus(self, position): 

        if self.head == None: 

            return 

        temp = self.head 

        if position == 0: 

            self.head = temp.next

            temp = None

            return 

        for i in range(position -1 ): 

            temp = temp.next

            if temp is None: 

                break

        if temp is None: 

            return 

        if temp.next is None: 

            return 

        next = temp.next.next

        temp.next = None

        temp.next = next 

    def cari(self, x): 

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

    

LL = Nodes() 

LL.tambahDepan(0)

LL.tambahDepan(4)

LL.tambahDepan(1)

LL.tambahAkhir(4)

LL.tambah(9,3)

print(LL.cari(9))

print(LL.cari(7))

LL.display()
