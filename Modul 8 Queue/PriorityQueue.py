import heapq
class PriorityQueue(object):
    def __init__(self):
        self.qlist= []
    def __len__(self):
        return len(self.qlist)
    def isEmpty(self):
        return len(self)==0
    def enqueue(self, data, prior):
        heapq.heappush(self.qlist, (prior, data))
        self.qlist.sort()
    def dequeue(self):
        return self.qlist.pop(0)
    def getFront(self):
        return self.qlist[0]
    def getRear(self):
        return self.qlist[-1]
    
S = PriorityQueue()

S.enqueue('Pisang', 3)
S.enqueue('Gedang', 1)
S.enqueue('Banana', 2)


print(S.qlist)
print("get front =",S.getFront())
print("get rear =",S.getRear())
S.dequeue()
print(S.qlist)
S.dequeue()
print(S.qlist)



