class Stack():
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self)==()

    def __len__(self):
        return len(self.items)

    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]

    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()

    def push(self,data):
        self.items.append(data)

s=Stack()

    
