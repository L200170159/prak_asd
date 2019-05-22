class Queue(object):
    def __init__(self):
        self.qlist = []
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self,data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.isEmpty()
        return self.qlist.pop(0)
    def getFront(self):
        return self.qlist[0]
    def getRear(self):
        return self.qlist[-1]

a = Queue()
a.enqueue('Gedang')
a.enqueue('Pisang')
a.enqueue('Banana')

print(a.qlist)


print("get front =",a.getFront())
print("get rear =",a.getRear())
