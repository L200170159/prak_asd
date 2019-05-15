from Stack import Stack
nilai=Stack()
for i in range(16):
    print(i,nilai.items)
    if i%3==0:
        nilai.push(i)
        
