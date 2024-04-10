class Queue:
    def __init__(self):
        self.qList = list()


    def isEmpty(self):
        return len(self.qList) == 0 

    def enqueue(self, item):
       self.qList.append(item)
        

    def len(self):
        return len(self.qList)
    
    def dequeue(self):
        if not self.isEmpty:
            return self.qList.pop(0)
        

        