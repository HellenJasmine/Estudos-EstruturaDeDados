
class QueueNode:
    def __init__(self, dado, prioridade):
        self.dado = dado
        self.prioridade = prioridade
        self.next = None



class Queue:
    def __init__(self):
        self.front = None 
        self.back = None 
        self.size = 0


    def isEmpty(self):
        return self.front is None
    
    def enqueue(self, elem):
        node = QueueNode(elem)
        if self.isEmpty():
            self.front = node
        else:
            self.back.next = node 

        self.back = node 
        self.size += 1 

    def len(self):
        if not self.isEmpty():
            return self.size
        
    
    def dequeue(self):
        if not self.isEmpty():
            node = self.front
            if self.front is self.back:
                self.front = None
            else:
                self.front = self.front.next


            self.size -= 1
            return node.dado 


    def enqueuePrioridade(self, tarefa, prioridade):
        node = QueueNode(tarefa, prioridade)
        if not self.isEmpty():
            if node.prioridade < self.front.prioridade:
                node.next = self.front
                self.front = node

            elif node.prioridade >= self.back.prioridade:
                self.back.next = node
                self.back = node


            else:
                temp = self.back
                ante = None
                while temp.prioridade >= node.prioridade:
                    ante = temp
                    temp = temp.next
                node.next = ante.next
                ante.next = node
        else:
            self.front = node 

            self.back = node 
        self.size += 1




    def mostar(self):
        if not self.isEmpty():
            temp = self.front
            while temp != None:
                print(f"{temp.dado} - dado | {temp.prioridade}- prioridade")
                temp = temp.next




fila = Queue()
fila.enqueuePrioridade("amor", 1)

fila.enqueuePrioridade("amor", 1)
fila.enqueuePrioridade("paz", 5)
fila.enqueuePrioridade("uniao", 3)
fila.enqueuePrioridade("paz", 0)
fila.enqueuePrioridade("joao", 2)
fila.enqueuePrioridade("oi", 4)
fila.mostar()
        
